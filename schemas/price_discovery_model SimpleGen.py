from pydantic import BaseModel, Field
from typing import Optional, Any
from typing import List, Optional

class DiscoveredModel_Navigationitem(BaseModel):
    name: Optional[str] = Field(..., description="")
    url: Optional[str] = Field(..., description="")

class DiscoveredModel_Modelsitem(BaseModel):
    name: Optional[str] = Field(..., description="")
    description: Optional[str] = Field(..., description="")

class DiscoveredModel(BaseModel):
    title: Optional[str] = Field(..., description="")
    navigation: Optional[List[DiscoveredModel_Navigationitem]] = Field(..., description="")
    models: Optional[List[DiscoveredModel_Modelsitem]] = Field(..., description="")