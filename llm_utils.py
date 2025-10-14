import os
from dotenv import load_dotenv
load_dotenv()  # Loads from .env by default

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

try:
    import ollama
except ImportError:
    ollama = None

import yaml


def load_config(config_file):
    with open(config_file, 'r') as f:
        return yaml.safe_load(f)


def get_provider_info(llm_alias, providers_file='providers.yaml'):
    providers = load_config(providers_file)['providers']
    for key, info in providers.items():
        if llm_alias in info.get('aliases', []) or key == llm_alias:
            return info['provider'], info['env_var']
    raise ValueError(f"LLM alias '{llm_alias}' not found in providers.yaml")


async def call_llm_directly(provider, api_token, prompt, extra_args):
    """Call LLM directly without crawling."""
    if provider.startswith("openai") or provider.startswith("openrouter"):
        if OpenAI is None:
            raise ImportError("OpenAI library not installed. Install with: pip install openai")
        base_url = "https://openai.com/v1" if provider.startswith("openai") else "https://openrouter.ai/api/v1"
        client = OpenAI(api_key=api_token, base_url=base_url)
        model = provider.split("/")[-1] if "/" in provider else provider
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            **extra_args
        )
        return response.choices[0].message.content.strip()
    elif provider.startswith("ollama"):
        if ollama is None:
            raise ImportError("Ollama library not installed. Install with: pip install ollama")
        model = provider.split("/")[-1]
        response = ollama.chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            options=extra_args
        )
        return response['message']['content'].strip()
    else:
        raise ValueError(f"Unsupported provider: {provider}")


async def prepare_and_call_llm(source, prompt):
    """Prepare LLM parameters and make the call."""
    llm_alias = source['llm']
    temperature = source.get('temperature', 0.0)
    top_p = source.get('top_p', 0.9)
    max_tokens = source.get('max_tokens', 8000)
    
    provider, env_var = get_provider_info(llm_alias)
    api_token = os.getenv(env_var) if env_var else None
    
    if api_token is None and not provider.startswith("ollama"):
        print(f"API token is required for {provider}. Skipping.")
        return None
    
    extra_args = {
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens
    }
    
    return await call_llm_directly(provider, api_token, prompt, extra_args)


def prepare_llm_config(source):
    """Prepare LLM configuration including provider, token, schema model, and extra args."""
    llm_alias = source.get('llm')
    if not llm_alias:
        return None, None, None, None
    
    provider, env_var = get_provider_info(llm_alias)
    api_token = os.getenv(env_var) if env_var else None
    
    # Load Pydantic schema model if provided
    schema_model = None
    pydantic_code = source.get('pydantic_model')
    if pydantic_code:
        try:
            exec(pydantic_code, globals())
            # Find the main class (not BaseModel itself)
            for name in list(globals().keys()):
                obj = globals()[name]
                if isinstance(obj, type) and issubclass(obj, BaseModel) and obj != BaseModel:
                    schema_model = obj
                    print(f"Using schema model: {name}")
                    break
            if not schema_model:
                print("No valid Pydantic model found in code")
        except Exception as e:
            print(f"Error loading Pydantic model: {e}")
    
    temperature = source.get('temperature', 0.0)
    top_p = source.get('top_p', 0.9)
    max_tokens = source.get('max_tokens', 8000)
    extra_args = {
        "temperature": temperature,
        "top_p": top_p,
        "max_tokens": max_tokens
    }
    
    return provider, api_token, schema_model, extra_args