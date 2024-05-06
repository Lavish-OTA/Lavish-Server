from sqlalchemy.orm import Session

from .schemas import NodeCreate, NodeUpdate
from ...db.model import Node


def add_node(db: Session, node: NodeCreate) -> Node:
    db_node = Node(serial_number=node.serial_number, type=node.type, description=node.description)
    db.add(db_node)
    db.commit()
    db.refresh(db_node)
    return db_node


def get_node(db: Session, node_id: int) -> Node:
    return db.query(Node).filter(Node.id == node_id).first()


def update_node(db: Session, node_id: int, node: NodeUpdate) -> Node:
    db_node = get_node(db, node_id)
    if db_node:
        db_node.type = node.type
        db_node.description = node.description
        db.commit()
        db.refresh(db_node)
    return db_node


def remove_node(db: Session, node_id: int):
    db_node = get_node(db, node_id)
    if db_node:
        db.delete(db_node)
        db.commit()
