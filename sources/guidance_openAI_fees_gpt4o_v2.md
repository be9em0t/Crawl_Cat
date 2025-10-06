Produce a compact JSON Schema (as a single JSON object) that describes the structured data present on the page. Requirements:

Include top-level title and description keys summarizing the purpose of the object.
For each property under properties include:
- type (string, integer, number, boolean, array, object)
- description: one concise human-readable sentence describing the field and when it appears
- examples: a short array with 1 example value (for objects/arrays include a representative instance)
If the field is an object, provide its own properties, required, and description keys and include examples for nested fields.
If the field is an array, specify items with a type and an examples array showing an example item.
Set required at the top-level and at nested object levels for fields that are always present. Use optional fields only when truly optional.
Keep the schema compact (avoid overly permissive additionalProperties: true unless necessary).
Add a top-level examples array containing one representative complete instance of the object (matching the schema).
Prefer concrete, narrow types (e.g., 'integer' for counts, 'number' for prices, 'string' for textual labels, 'boolean' for flags).

Important: this page contains pricing and model names. Do NOT omit any pricing or model-related information. Specifically ensure the schema includes a top-level `models` array (or equivalent) describing each model found on the page. For each model entry include at minimum the following fields when present on the page:
- `model_name` (string)
- `input_cost` (number or string, e.g. 0.03)
- `output_cost` (number or string)
- `units` (string, e.g. "USD per 1K tokens")
- `notes` (string, optional: additional tier/availability notes)

Also extract other fee entries (realtime, image generation, responses API, assistants, subscription tiers, priority processing), and include them under explicit properties (e.g. `realtime`, `image_generation`, `responses`, `assistants`, `subscription`) with structured subfields for costs and units.

Glossary requirement: produce a `glossary` object that lists every field name you put in the schema, with a one-line description and one example for each. The glossary must not omit fields that appear on the page.

Return only the raw JSON object (no explanation, no markdown/code fences).

Do NOT wrap the JSON in markdown or code fences (e.g. ```json). Return the raw JSON object only, with no surrounding text or formatting.