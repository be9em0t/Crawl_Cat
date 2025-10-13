from pydantic import BaseModel
from typing import List, Optional

class Node(BaseModel):
    name: str
    url: str
    description: str

class Subcategory(BaseModel):
    name: str
    anchor: Optional[str] = None
    nodes: List[Node]

class Category(BaseModel):
    name: str
    url: str
    description: str
    subcategories: List[Subcategory]

class NodeLibrary(BaseModel):
    name: str
    url: str
    description: str
    categories: List[Category]