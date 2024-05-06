from pydantic import BaseModel


class FirmwareBase(BaseModel):
    version: str
    description: str | None = None


class FirmwareCreate(FirmwareBase):
    binary_file_path: str


class FirmwareRead(FirmwareBase):
    id: int
    binary_file_path: str

    class Config:
        from_attributes = True
