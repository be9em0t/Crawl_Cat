Prompt and settings to extract model pricing and glossary from pricing pages. Require models array with model_name, input_cost, output_cost, units, notes; require glossary listing all fields

Guidance: `Return a strict JSON array that represents the ShaderGraph structure`.
  The top-level value MUST be a JSON array of topic objects. Each topic object must have:
    - "topic": string
    - "categories": an array of category objects
  Each category object must have:
    - "category": string
    - "nodes": an array of node name strings

Rules:
  - If a topic has zero categories, represent it as a single category with the topic name.
    Example: {"topic": "Channel", "categories": [{"category": "Channel", "nodes": ["Combine Channels", "Split Channels"]}]}
  - Do NOT include any descriptions, explanations, or extra text outside the JSON array.
  - Only return valid JSON (no Markdown, no commentary). 

Example top-level shape:
  [
    {
      "topic": "Artistic",
      "categories": [
        {"category": "Adjustment", "nodes": ["Channel Mixer", "Contrast"]},
        {"category": "Blend", "nodes": ["Blend Node A", "Blend Node B"]}
      ]
    },
    {
      "topic": "Channel",
      "categories": [{"category": "Channel", "nodes": ["Combine Channels", "Split Channels"]}]
    }
  ]

Make the JSON precise: include all topics, categories and node names found on the page in the structure above.
