
python schema_discovery.py --provider gpt4o --url 'https://openai.com/api/pricing/' --out price_discovery

py crawl-cat.py -p gpt4o --pymodel schemas/openai_price_discovered_model.py

---
# Pydantic schema generation prompt:

pydantic_model: |
	root: Shadergraph Node Library
	├── Graph nodes (9 categories in total)
	│   │   ├── Sub-category: Adjustment
	│   │   │   ├── Node: Channel Mixer Node; Description: Controls the amount each of the channels of...
	│   │   │   ├── Node: Contrast Node; Description: Adjusts the contrast of...
	│   │   │   └── (... other nodes with descriptions)
	│   │   ├── Sub-category: Blend
	│   │   │   └── Blend Node; Description: Blends the value of...
	│   │   ├── Sub-category: Filter
	│   │   │   └── (... other nodes with descriptions)
	│   │   └── (... other sub-categories, containing nodes with descriptions)
	│   ├── Topic: Channel
	│   │   ├── Node: Append Node; Description: Creates a new vector Out by... 
	│   │   ├── Node: Combine Node; Description: Creates new vectors from... 
	│   │   └── (... other nodes with descriptions)
	│   ├── Topic: Custom Render Texture nodes
	│   │   └── (... other sub-categories OR nodes)
	│   └── (...9 topics in total)
	└── Block nodes

in our documentation crawler we need to set up documentation extraction for Unity ShaderGrpah Nodes:
https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html

To that end, we need to provide in #file:config_unity_shadergraph.yaml a correct pydantic model for Crawl4ai to consume .

In the yaml file, In the pydantic_model key I have stored a tree graph of the structure. Please work out a correct Pydantic model that reflects these requrements: 
1. follows the provided structure in pydantic_model key. Replace the structure with the correct pydantic model
2. reflects the Unity ShaderGrpah Nodes pages at https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html 
3. is similar to the models in #file:config_openai_fees.yaml 
4. works with multi-page source: the provided URL contains links to sub-pages, that contain either another sub-categories or shadergraph nodes. 
5. each branch should end in one or more nodes!

---
# old guidance + prompt:

def build_schema_prompt(url: str, html_snippet: str) -> str:
    guidance = (
        "Produce a compact JSON Schema (as a single JSON object) that describes the structured data present on the page. "
        "Return only the raw JSON object (no explanation, no markdown or fences). Include a top-level `examples` array with one example instance. "
        "Ensure the schema contains a `models` array describing model entries when present on the page."
    )
    guidance = guidance + " Do NOT wrap the JSON in markdown or code fences. Return the raw JSON object only."
    prompt = (
        f"You are given the HTML content of a web page (URL: {url}).\n"
        "Analyze the content and propose a compact JSON Schema that describes the data a user would want to extract from this page.\n\n"
        f"Guidance: {guidance}\n\n"
        "Page HTML (trimmed):\n"
        f"{html_snippet}\n\n"
        "Return a single JSON object (the JSON Schema). Do not include any explanation."
    )
    return prompt

---
Crawl instruction:

"""From the crawled content, extract all mentioned model names along with their fees for input and output tokens. \nDo not miss any models in the entire content."""
