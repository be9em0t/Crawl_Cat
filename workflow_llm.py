import os
import json
import yaml
import llm_utils
import save_utils
from pydantic import BaseModel

async def workflow_llm(source, urls):
    llm_alias = source['llm']
    provider, env_var = llm_utils.get_provider_info(llm_alias)
    api_token = os.getenv(env_var) if env_var else None
    
    instruction = source.get('instruction', '')
    schema_model = None
    if 'pydantic_model' in source and source['pydantic_model']:
        exec(source['pydantic_model'], globals())
        # Find the main class (assume NodeLibrary)
        main_class = 'NodeLibrary'
        if main_class in globals():
            schema_model = globals()[main_class]
        else:
            # Find any class
            for name in globals():
                if isinstance(globals()[name], type) and issubclass(globals()[name], BaseModel):
                    schema_model = globals()[name]
                    break
            else:
                raise ValueError("No Pydantic model class found in generated code")
    
    extraction_type = source.get('extraction_type', 'schema')
    extra_args = {
        "temperature": source.get('temperature', 0),
        "top_p": source.get('top_p', 0.9),
        "max_tokens": source.get('max_tokens', 2000)
    }
    output_file = source.get('out_file', 'extracted')
    workflow = source.get('workflow', 'llm')
    output_file = f"{output_file}_{workflow}"
    if not output_file.endswith('.json'):
        output_file += '.json'
    css_selector = source.get('css_selector')
    headless = source.get('headless', True)
    cache_mode = source.get('cache_mode', 'BYPASS')
    word_count_threshold = source.get('word_count_threshold', 1)
    page_timeout = source.get('page_timeout', 80000)
    
    await llm_utils.extract_structured_data_using_llm(
        provider=provider,
        api_token=api_token,
        urls=urls,
        instruction=instruction,
        schema_model=schema_model,
        extra_args=extra_args,
        headless=headless,
        cache_mode=cache_mode,
        word_count_threshold=word_count_threshold,
        page_timeout=page_timeout,
        output_file=output_file,
        css_selector=css_selector,
        extraction_type=extraction_type
    )