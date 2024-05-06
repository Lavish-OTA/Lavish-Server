from typing import List

from fastapi import APIRouter, File, UploadFile, status

from .crud import upload_firmware, assign_firmware, get_firmware_history
from .schemas import FirmwareCreate, FirmwareRead

firmware_router = APIRouter()


@firmware_router.post("/", response_model=FirmwareRead, status_code=status.HTTP_201_CREATED)
def upload_firmware_endpoint(firmware: FirmwareCreate, file: UploadFile = File(...)):
    """Upload a new firmware binary"""
    return upload_firmware(firmware, file)


@firmware_router.post("/assign/{node_id}", status_code=status.HTTP_202_ACCEPTED)
def assign_firmware_endpoint(node_id: int, firmware_id: int):
    """Assign firmware to a specific node"""
    assign_firmware(node_id, firmware_id)
    return {"message": "Firmware assignment successful"}


@firmware_router.get("/history/{node_id}", response_model=List[FirmwareRead])
def get_firmware_history_endpoint(node_id: int):
    """Retrieve firmware update history for a node"""
    return get_firmware_history(node_id)
