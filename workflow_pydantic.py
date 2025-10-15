import os
import json
import llm_utils
import save_utils
from pydantic import BaseModel

async def workflow_pydantic(source, urls):
    out_file = source.get('out_file', 'pydantic_output')
    workflow = source.get('workflow', 'pydantic')
    out_file_with_workflow = f"{out_file}_{workflow}"
    
    # Look for explore outputs (assuming they have _explore suffix)
    explore_base = out_file  # The base name without workflow
    explore_md_path = f"output/{explore_base}_explore.md"
    explore_json_path = f"output/{explore_base}_explore.json"
    
    if not os.path.exists(explore_md_path) or not os.path.exists(explore_json_path):
        raise ValueError(f"Explore outputs not found: {explore_md_path} and {explore_json_path}. Run explore workflow first with out_file: '{explore_base}'.")
    
    with open(explore_md_path, 'r') as f:
        explore_md = f.read()
    
    with open(explore_json_path, 'r') as f:
        explore_json = json.load(f)
    
    # Get the prompt from config
    base_prompt = source.get('prompt', '')
    
    # Build the full prompt including the data
    prompt = base_prompt + f"\n\nExplore Markdown (truncated if necessary):\n{explore_md[:10000]}...\n\nExplore JSON (first 5 pages):\n{json.dumps(explore_json[:5], indent=2)}"
    
    llm_alias = source['llm']
    temperature = source.get('temperature', 0.0)
    top_p = source.get('top_p', 0.9)
    max_tokens = source.get('max_tokens', 8000)
    
    provider, env_var = llm_utils.get_provider_info(llm_alias)
    api_token = os.getenv(env_var) if env_var else None
    
    if api_token is None and not provider.startswith("ollama"):
        print(f"API token is required for {provider}. Skipping.")
        return
    
    extra_args = {
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens
    }
    
    # Call LLM directly with the prompt
    model_code = await llm_utils.call_llm_directly(provider, api_token, prompt, extra_args)
    
    # Clean the model_code by removing markdown code blocks
    if model_code.startswith('```python'):
        model_code = model_code[9:]
    if model_code.endswith('```'):
        model_code = model_code[:-3]
    model_code = model_code.strip()
    
    # Save the model code
    model_file = f"output/{out_file_with_workflow}_model.py"
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
        
        # Now, use the model for extraction
        await llm_utils.extract_structured_data_using_llm(
            provider=provider, 
            api_token=api_token, 
            urls=urls, 
            instruction=source.get('instruction', ''), 
            schema_model=ModelClass, 
            extra_args=extra_args,
            headless=source.get('headless', True),
            cache_mode=source.get('cache_mode', 'BYPASS'),
            word_count_threshold=source.get('word_count_threshold', 1),
            page_timeout=source.get('page_timeout', 80000),
            output_file=f"{out_file}_pydantic.json",
            css_selector=source.get('css_selector'),
            extraction_type="schema"
        )
        
    except Exception as e:
        print(f"Error processing generated model or extracting: {e}")
        # Save empty structured JSON
        save_utils.save_json(f"output/{out_file}_pydantic.json", {})