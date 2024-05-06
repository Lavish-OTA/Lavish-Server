from pydantic import BaseModel


class NodeBase(BaseModel):
    serial_number: str
    type: str
    description: str | None = None


class NodeCreate(NodeBase):
    pass


class NodeUpdate(BaseModel):
    type: str | None = None
    description: str | None = None


class NodeRead(NodeBase):
    id: int
    firmware_id: int | None

    class Config:
        from_attributes = True
