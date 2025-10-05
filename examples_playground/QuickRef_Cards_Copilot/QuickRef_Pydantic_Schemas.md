Pydantic Schemas — Quick Reference

Big picture
- Pydantic model = the editable, runtime Python class you write and maintain (source-of-truth).
- Pydantic schema / JSON Schema = machine-readable representation generated from the model (what you feed to LLMs or other tools).
- Use models to validate LLM or CSS extraction output; use generated JSON Schema to instruct the LLM.

Declaring & validating data
- Declare models (Pydantic v2 style):

```python
from pydantic import BaseModel, Field
class OpenAIModelFee(BaseModel):
    model_name: str = Field(..., description="Name of the model")
    input_fee: str
    output_fee: str
```

- Validate LLM output:
  - parse/convert JSON: `payload = json.loads(llm_output)`
  - validate: `obj = OpenAIModelFee.model_validate(payload)` (v2) or `OpenAIModelFee.parse_obj(payload)` (v1)
  - handle `ValidationError` for feedback / human review.

- For top-level lists or single-value roots use `RootModel` or wrap in a container model:

```python
class PricingDoc(BaseModel):
    source_url: str
    models: list[OpenAIModelFee]
```

Discriminators & multiple page types
- Include a small discriminator field (recommended `kind`).

Example:

```python
from typing import Annotated, Union, Literal
from pydantic import BaseModel, Field

class ApiRef(BaseModel):
    kind: Literal['api_ref']
    name: str

class Tutorial(BaseModel):
    kind: Literal['tutorial']
    steps: list[str]

Page = Annotated[Union[ApiRef, Tutorial], Field(discriminator='kind')]
```

Extraction types / modes
- schema — LLM returns JSON conforming to JSON Schema / Pydantic model (strict; easiest to validate).
- function_call / response_schema — provider-enforced structured outputs (when supported).
- json — LLM returns JSON but not strongly typed (validate afterwards).
- classification — LLM returns a label used to route to a schema.
- css/xpath/regex — deterministic DOM extraction (no LLM).
- chunked-schema / chunk-and-merge — split large pages, extract per chunk, then merge.
- post-process/repair — second-pass LLM to fix validation errors.

LLM-driven schema generation (create_model / dynamic models)
- Ask LLM to return JSON Schema (not raw Python).
- Programmatically validate the returned JSON Schema.
- Convert to a Pydantic model using `pydantic.create_model` or use a code generator like `datamodel-code-generator`.
- Validate using sample outputs; require human review before persisting as canonical Python.

Minimal runtime example (flat object -> create_model):

```python
from pydantic import create_model
from typing import Optional

props = {
    'model_name': (Optional[str], ...),
    'input_fee': (Optional[str], ...),
    'output_fee': (Optional[str], ...),
}
DynamicModel = create_model('DynamicModel', **props)
```

Practical workflow (safe, production-ready)
1. Author small focused Pydantic models per page-type in `schemas/` (source of truth).
2. Generate JSON Schema for prompting: `json_schema = MyModel.model_json_schema()` (v2).
3. Prompt LLM with a short instruction + JSON Schema + 1 example. Use `temperature=0`.
4. Parse LLM output -> `json.loads(...)` -> `MyModel.model_validate(...)`.
5. If validation fails: retry with correction prompt or flag for human review.
6. For multi-page docs: use deterministic URL-based `page_rules` first; fallback to LLM classifier only when needed.
7. Log raw LLM output, generated schema, and validation traces for auditing.

Tips & gotchas
- Keep schemas small and focused.
- Always validate LLM output; never trust it implicitly.
- For unions: include `kind` discriminator.
- For large pages: use CSS selectors or chunking to reduce token usage.
- Use provider-schema/function_call features when available for stricter enforcement.

One-line checklist before running extraction
- Do I have a model for this page type? Yes -> use it.
- Can I match by URL pattern? Yes -> deterministic route.
- If not matched, do I classify first or run LLM extraction directly? Choose classifier then schema.
- Always run `model_validate` and decide auto-accept vs manual review policy.
