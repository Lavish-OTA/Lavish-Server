from fastapi import APIRouter, HTTPException, status

from .crud import add_node, get_node, update_node, remove_node
from .schemas import NodeCreate, NodeRead, NodeUpdate

node_router = APIRouter()


@node_router.post("/", response_model=NodeRead, status_code=status.HTTP_201_CREATED)
def add_node_endpoint(node: NodeCreate):
    """Register a new node"""
    return add_node(node)


@node_router.get("/{node_id}", response_model=NodeRead)
def get_node_endpoint(node_id: int):
    """Retrieve details about a specific node"""
    node = get_node(node_id)
    if node is None:
        raise HTTPException(status_code=404, detail="Node not found")
    return node


@node_router.put("/{node_id}", response_model=NodeRead)
def update_node_endpoint(node_id: int, node: NodeUpdate):
    """Update node information"""
    return update_node(node_id, node)


@node_router.delete("/{node_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_node_endpoint(node_id: int):
    """Delete a node"""
    remove_node(node_id)
    return {"message": "Node removed successfully"}
