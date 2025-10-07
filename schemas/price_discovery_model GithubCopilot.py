"""Pydantic model tuned for OpenAI pricing page extraction.

This file defines structured types for model pricing entries found on
https://openai.com/api/pricing/. It is written to be compatible with
Pydantic v1 (the project's requirements pin pydantic>=1.10,<3).

Features:
- Nested, explicit types for model pricing entries (input/cached/output/training)
- Validators that parse raw cost strings like "$0.03 / 1K tokens" into numeric
  value and units for easier downstream use.
- Helper `get_json_schema()` that returns a JSON schema dict whether Pydantic
  v1 or v2 is installed (handles both `schema()`/`schema_json()` and
  `model_json_schema()`). This avoids warnings where code expects
  `model_json_schema()`.
"""

from __future__ import annotations

from typing import Optional, Any, List, Dict
import re
from pydantic import BaseModel, Field, validator


_PRICE_RE = re.compile(r"\$?\s*([0-9,.]+)\s*(?:/\s*([^\n]+))?")


class PriceEntry(BaseModel):
	"""Represents a single price string and parsed numeric/unit values.

	Example raw strings found on the page:
	  - "$1.25 / 1M tokens"
	  - "$0.125 / 1M tokens"
	  - "$100.00 / training hour"
	"""

	raw: Optional[str] = Field(None, description="Original raw price string captured from page")
	value: Optional[float] = Field(None, description="Parsed numeric amount (float).")
	unit: Optional[str] = Field(None, description="Unit text (e.g. '1M tokens', '1K calls', 'training hour').")

	@validator("raw", pre=True, always=True)
	def _parse_raw(cls, v, values):
		# if raw is empty, leave value/unit None
		if not v:
			return v
		if isinstance(v, str):
			m = _PRICE_RE.search(v)
			if m:
				num = m.group(1).replace(",", "")
				try:
					values.setdefault("value", float(num))
				except Exception:
					values.setdefault("value", None)
				unit = m.group(2)
				values.setdefault("unit", unit.strip() if unit else None)
		return v


class ModelPricing(BaseModel):
	"""Structured model entry capturing pricing and metadata."""

	model_name: Optional[str] = Field(None, description="Model identifier or display name")
	title: Optional[str] = Field(None, description="Short title or headline for the model")
	description: Optional[str] = Field(None, description="Short description paragraph")
	model_type: Optional[str] = Field(None, description="Category: flagship/realtime/image/etc.")

	input: Optional[PriceEntry] = Field(None, description="Input price entry")
	cached_input: Optional[PriceEntry] = Field(None, description="Cached input price entry")
	output: Optional[PriceEntry] = Field(None, description="Output price entry")
	training: Optional[PriceEntry] = Field(None, description="Training/fine-tuning price, when present")

	notes: Optional[str] = Field(None, description="Any availability/tier/notes text associated with the model")
	api: Optional[str] = Field(None, description="API name or endpoint associated with this model (e.g. 'Realtime', 'Responses')")


class PricingPage(BaseModel):
	"""Top-level representation of the pricing page.

	The page contains many sections; we focus on model listings and common
	API sections. The lists are permissive (Optional[List[...]]) so missing
	sections do not fail parsing.
	"""

	page_title: Optional[str] = Field(None, description="Page title")
	models: Optional[List[ModelPricing]] = Field(None, description="List of model pricing entries")
	realtime: Optional[List[ModelPricing]] = Field(None, description="Realtime API models/prices")
	image_generation: Optional[List[ModelPricing]] = Field(None, description="Image generation models/prices")
	other_sections: Optional[Dict[str, Any]] = Field(None, description="Catch-all for other structured entries (tools, agents, etc.)")

	def get_json_schema(self) -> Dict[str, Any]:
		"""Return a JSON schema dict in a Pydantic-version-agnostic way.

		- Pydantic v2 provides Model.model_json_schema();
		- Pydantic v1 provides Model.schema() / Model.schema_json().

		This helper attempts v2 first, then falls back to v1.
		"""

		# prefer v2 API if available
		try:
			# type: ignore[attr-defined]
			return self.__class__.model_json_schema()
		except Exception:
			pass

		# fallback to pydantic v1 style
		try:
			return self.__class__.schema()
		except Exception:
			# last resort: build a minimal manual schema
			return {"title": self.__class__.__name__}


__all__ = ["PriceEntry", "ModelPricing", "PricingPage"]


