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

# Example usage
if __name__ == "__main__":
    import json

    # Load the hierarchical JSON
    with open('output/shadergraph_hierarchy.json', 'r') as f:
        data = json.load(f)

    # Validate and parse with Pydantic
    library = NodeLibrary(**data)
    print(f"Loaded Node Library: {library.name}")
    print(f"Number of categories: {len(library.categories)}")

    # Print some examples
    for cat in library.categories[:2]:  # First 2 categories
        print(f"\nCategory: {cat.name}")
        for sub in cat.subcategories[:1]:  # First subcategory
            print(f"  Subcategory: {sub.name} ({len(sub.nodes)} nodes)")
            for node in sub.nodes[:2]:  # First 2 nodes
                print(f"    Node: {node.name} - {node.url}")

    print("\nPydantic models generated successfully!")