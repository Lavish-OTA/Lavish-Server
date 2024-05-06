from sqlalchemy.orm import Session

from .schemas import FirmwareCreate
from ...db.model import Node, Firmware


def upload_firmware(db: Session, firmware: FirmwareCreate, file_data) -> Firmware:
    db_firmware = Firmware(version=firmware.version, description=firmware.description, binary_file=file_data)
    db.add(db_firmware)
    db.commit()
    db.refresh(db_firmware)
    return db_firmware


def assign_firmware(db: Session, node_id: int, firmware_id: int):
    db_firmware = db.query(Firmware).filter(Firmware.id == firmware_id).first()
    db_node = db.query(Node).filter(Node.id == node_id).first()
    if db_node and db_firmware:
        db_node.firmware_id = firmware_id
        db.commit()


def get_firmware_history(db: Session, node_id: int):
    return db.query(Firmware).join(Node).filter(Node.id == node_id).all()
