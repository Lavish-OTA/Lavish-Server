from fastapi import APIRouter

from .firmware.router import firmware_router
from .nodes.router import node_router
from .users.router import user_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/users", tags=["Users"])
api_router.include_router(node_router, prefix="/nodes", tags=["Nodes"])
api_router.include_router(firmware_router, prefix="/firmware", tags=["Firmware"])
