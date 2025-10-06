from pydantic import BaseModel, Field
from typing import Optional, Any
from typing import List, Optional

class DiscoveredModel_Modelsitem_Pricing(BaseModel):
    input: Optional[str] = Field(..., description="")
    cached_input: Optional[str] = Field(..., description="")

class DiscoveredModel_Modelsitem(BaseModel):
    name: Optional[str] = Field(..., description="")
    description: Optional[str] = Field(..., description="")
    pricing: Optional[DiscoveredModel_Modelsitem_Pricing] = Field(..., description="")

class DiscoveredModel(BaseModel):
    title: Optional[str] = Field(..., description="")
    models: Optional[List[DiscoveredModel_Modelsitem]] = Field(..., description="")