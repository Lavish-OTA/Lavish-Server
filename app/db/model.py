from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    name = Column(String, index=True)


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True, index=True)
    serial_number = Column(String, unique=True, index=True)
    type = Column(String, nullable=False)
    description = Column(String, nullable=True)
    firmware_id = Column(Integer, ForeignKey('firmware.id'))
    firmware = relationship("Firmware", back_populates="nodes")


class Firmware(Base):
    __tablename__ = "firmware"
    id = Column(Integer, primary_key=True)
    version = Column(String, nullable=False)
    description = Column(String)
    binary_file_path = Column(String, nullable=False)
    nodes = relationship("Node", back_populates="firmware")
