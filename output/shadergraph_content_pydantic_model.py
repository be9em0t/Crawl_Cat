from typing import List, Optional
from pydantic import BaseModel, Field

class Node(BaseModel):
    name: str = Field(..., description="The name of the node.")
    url: str = Field(..., description="The URL of the node documentation.")
    description: str = Field(..., description="A brief description of the node.")

class Subcategory(BaseModel):
    name: str = Field(..., description="The name of the subcategory.")
    anchor: str = Field(..., description="The anchor link for the subcategory.")
    nodes: List[Node] = Field(default_factory=list, description="A list of nodes in this subcategory.")

class Category(BaseModel):
    name: str = Field(..., description="The name of the category.")
    url: str = Field(..., description="The URL of the category documentation.")
    description: str = Field(..., description="A brief description of the category.")
    subcategories: Optional[List[Subcategory]] = Field(default=None, description="A list of subcategories under this category.")
    nodes: Optional[List[Node]] = Field(default=None, description="A list of nodes in this category.")

class NodeLibrary(BaseModel):
    categories: List[Category] = Field(..., description="A list of categories in the Node Library.")