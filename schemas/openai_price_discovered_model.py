from pydantic import BaseModel, Field
from typing import List, Optional

class DiscoveredModel(BaseModel):
    models: Optional[List[dict]] = Field(..., description="")