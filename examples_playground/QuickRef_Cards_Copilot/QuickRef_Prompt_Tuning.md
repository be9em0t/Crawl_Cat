## Example Crawl Mode implementation guidelines
- Mode name is "Unity ShaderGraph"
- Unity ShaderGraph mapping note: the top-level "topics" correspond to the major sections of the ShaderGraph Node Library (e.g., "Artistic", "Channel"), categories are the sub-groups within those sections, and nodes are objects with `name` and `description` fields.

- URL is "https://docs.unity3d.com/Packages/com.unity.shadergraph@17.4/manual/Node-Library.html" 
- Capturing requirements:
  - Node library has topics, categories and nodes
  - we want to capture all nodes in the correct category structure
  - a category always contains nodes, otherwise it's just a topic
  - a topic can have zero or more categories 
  - if a topic has zero categories it itself is the category
Use this example as a stating point.
Graph nodes:
Artistic topic:
  - Adjustment category:
    - Channel Mixer node
    - Contast node
    - ...
  - Blend category
    - ...
  - Filter category
    - ...
  - Mask category
    - ...
  - Normal category
    - ...
  - Utility category
    - ...
Channel topic = Channel category:
  - Combine Channels
  - Split Channels
  - Reorder Channels
  - Flip Channels
Custom Render Texture topic = Custom Render Texture category:
  - ... 
Input topic = Input category:
  - ... 
Math topic = Math category:
  - ...
Procedural topic = Procedural category:
  - ...
Utility topic = Utility category:
  - ...
UV topic = UV category:
  - ...


## LLM tuning guidance (quick)

You can tune LLM behavior via the YAML `params` block:

- `temperature` (float): controls randomness. Use `0.0` for deterministic structure extraction. Small values like `0.0 - 0.2` are recommended.
- `max_tokens` (int): budget for the LLM response. For structure-only JSON extracts 512–1024 is often enough. Large values (e.g. 3000) are only needed for very verbose outputs and can approach model context limits.
- `chunk_token_threshold` (int): page token size above which the page is split into chunks. Increase this to reduce the number of LLM calls for large documentation pages if your model has a large context window (e.g. 8000 or 24000). Lower values make more, smaller requests.
- `apply_chunking` (bool): enable or disable chunking. Disable only if you are sure the entire page fits comfortably in your model's context window.
- `overlap_rate` (float 0.0-1.0): small overlap (0.05–0.15) between chunks helps avoid missed items across chunk boundaries but increases token usage.

Example `params` tuned for a large docs site when using a model with an 8k+ token window:

```yaml
params:
  temperature: 0.0
  max_tokens: 1024
  chunk_token_threshold: 8000
  apply_chunking: true
  overlap_rate: 0.1
```

If you use a model with a larger context (24k–32k), consider increasing `chunk_token_threshold` accordingly and keep `max_tokens` conservative so prompt + response stay within the model's context limit.

Note: provider/model context windows differ. Check your provider's model docs (OpenAI/Anthropic/HuggingFace) and tune `chunk_token_threshold` and `max_tokens` so prompt_size + max_tokens < model_context_size (leave a small margin).

## Prompting for crawl4ai (quick)

Crawl4ai's LLM-driven extraction is prompt-sensitive. Keep prompts short, explicit, and machine-parseable. These short, practical guidelines are tuned for reliable structure and DOM discovery:

- Start with a JSON schema or explicit structure example. If you provide a schema, request the LLM to return only JSON that conforms to it. This reduces hallucinations and parsing edge-cases.
  Example: "Return a strict JSON array of topic objects. Each topic must have 'topic' (string) and 'categories' (array). Each category must have 'category' and 'nodes' (array of strings). Return only valid JSON."
- When asking for DOM selectors, ask for both index-page selectors and node-page selectors separately and insist on returning a strict JSON object with named fields `index_selectors` and `node_page_selectors`.
- Prioritize deterministic selectors first: request the LLM to prefer stable IDs, named classes, or anchor link patterns (e.g., `#main .node-list a`), and fall back to heading+paragraph heuristics as a secondary option.
- Include corrective examples when the schema can vary. Show one or two valid minimal examples inline so the LLM can mimic the shape precisely.
- Ask the model to avoid extraneous text: "Only return JSON, no commentary, no Markdown." This makes extraction and validation deterministic.
- Validate the LLM output immediately: parse the JSON and run a quick shape-check. If parsing fails, retry once with an instruction to strictly conform to the schema.

Short prompt pattern (compact):

"Instruction: Return a strict JSON array matching this schema: [example schema here]. Return only valid JSON. If any field is missing, return an empty string for it."

These conventions keep crawl4ai runs predictable and make downstream merging/heuristics (DOM scraping and enrichment) simpler.

## Schema (quick)

Nodes include descriptions:

```json
[
  {
    "topic": "Artistic",
    "categories": [
      {
        "category": "Adjustment",
        "nodes": [
          {"name": "Channel Mixer", "description": "Mixes color channels together."},
          {"name": "Contrast", "description": "Adjusts image contrast."}
        ]
      }
    ]
  }
]
```

