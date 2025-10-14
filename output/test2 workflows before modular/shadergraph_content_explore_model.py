from typing import List, Optional
from pydantic import BaseModel, Field

class Node(BaseModel):
    name: str = Field(..., description="The name of the node.")
    url: Optional[str] = Field(None, description="The URL of the node documentation.")
    description: Optional[str] = Field(None, description="A brief description of the node.")

class Subcategory(BaseModel):
    name: str = Field(..., description="The name of the subcategory.")
    anchor: Optional[str] = Field(None, description="An optional anchor for the subcategory.")
    nodes: List[Node] = Field(..., description="A list of nodes in this subcategory.")

class Category(BaseModel):
    name: str = Field(..., description="The name of the category.")
    url: Optional[str] = Field(None, description="The URL of the category documentation.")
    description: Optional[str] = Field(None, description="A brief description of the category.")
    subcategories: Optional[List[Subcategory]] = Field(None, description="A list of subcategories under this category.")
    nodes: Optional[List[Node]] = Field(None, description="A list of nodes in this category.")

class NodeLibrary(BaseModel):
    graph_nodes: List[Category] = Field(..., description="A list of categories containing graph nodes.")