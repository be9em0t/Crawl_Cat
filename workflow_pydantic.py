import os, sys
from dotenv import load_dotenv
load_dotenv()  # Loads from .env by default

import asyncio
import json
import yaml
from typing import Dict, List
from pydantic import BaseModel, Field
import save_utils
from llm_utils import load_config, get_provider_info, call_llm_directly, prepare_and_call_llm


async def workflow_pydantic(source, urls):
    out_file_base = source.get('out_file', 'pydantic_output')
    workflow = source['workflow']
    out_file = f"{out_file_base}_{workflow}"
    explore_out_file = f"{out_file_base}_explore"
    explore_md_path = f"output/{explore_out_file}.md"
    explore_json_path = f"output/{explore_out_file}.json"
    
    if not os.path.exists(explore_md_path) or not os.path.exists(explore_json_path):
        raise ValueError(f"Explore outputs not found: {explore_md_path} and {explore_json_path}. Run explore workflow first with out_file: '{out_file_base}'.")
    
    with open(explore_md_path, 'r') as f:
        explore_md = f.read()
    
    with open(explore_json_path, 'r') as f:
        explore_json = json.load(f)
    
    # Get the prompt from config
    base_prompt = source.get('prompt', '')
    
    # Build the full prompt including the data
    prompt = base_prompt + f"\n\nExplore Markdown (truncated if necessary):\n{explore_md[:10000]}...\n\nExplore JSON (first 5 pages):\n{json.dumps(explore_json[:5], indent=2)}"
    
    # Call LLM directly with the prompt
    model_code = await prepare_and_call_llm(source, prompt)
    
    # Clean the model_code by removing markdown code blocks
    if model_code.startswith('```python'):
        model_code = model_code[9:]
    if model_code.endswith('```'):
        model_code = model_code[:-3]
    model_code = model_code.strip()
    
    # Save the model code
    model_file = f"output/{out_file}_model.py"
    with open(model_file, 'w') as f:
        f.write(model_code)
    print(f"Saved Pydantic models to {model_file}")
    
    # Execute the model code to get the classes
    try:
        exec(model_code, globals())
        # Find the main class (assume NodeLibrary)
        main_class = 'NodeLibrary'
        if main_class in globals():
            ModelClass = globals()[main_class]
        else:
            # Find any class
            for name in globals():
                if isinstance(globals()[name], type) and issubclass(globals()[name], BaseModel):
                    ModelClass = globals()[name]
                    break
            else:
                raise ValueError("No Pydantic model class found in generated code")
        
        print(f"Using model class: {ModelClass.__name__}")
        
        # Use the explore markdown to build hierarchical structure with LLM
        build_prompt = f"""
Using the generated Pydantic model schema, analyze the combined explore markdown content and construct the hierarchical NodeLibrary structure.

Model schema: {json.dumps(ModelClass.model_json_schema())}

CRITICAL REQUIREMENTS:
- Capture EVERY SINGLE node from ALL categories and subcategories present in the content
- Do not miss any nodes - include all nodes even if there are hundreds
- Parse the complete hierarchical structure of categories, subcategories, and nodes
- Ensure comprehensive coverage across all pages in the content
- Count and verify you have captured all nodes mentioned
- The output JSON MUST have a top-level key 'graph_nodes' containing the list of categories

The markdown contains content from all crawled pages. Parse the hierarchical structure of categories, subcategories, and nodes.

Output only the JSON object matching the NodeLibrary schema with 'graph_nodes' as the root key.

Combined Markdown Content (truncated):
{explore_md[:300000]}...
"""
        
        hierarchical_json_str = await prepare_and_call_llm(source, build_prompt)
        
        # Clean the JSON
        if hierarchical_json_str.startswith('```json'):
            hierarchical_json_str = hierarchical_json_str[7:]
        if hierarchical_json_str.endswith('```'):
            hierarchical_json_str = hierarchical_json_str[:-3]
        hierarchical_json_str = hierarchical_json_str.strip()
        
        try:
            hierarchical_data = json.loads(hierarchical_json_str)
            # Validate with the model
            validated = ModelClass(**hierarchical_data)
            final_data = validated.model_dump()
            print("Successfully validated hierarchical structure")
        except Exception as e:
            print(f"Validation failed: {e}. Using raw data.")
            final_data = json.loads(hierarchical_json_str)
        
        save_utils.save_json(f"output/{out_file}.json", final_data)
        
    except Exception as e:
        print(f"Error processing generated model or extracting: {e}")
        # Save empty structured JSON
        save_utils.save_json(f"output/{out_file}.json", {})