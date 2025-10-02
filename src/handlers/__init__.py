from .common import common_router  # Добавляем новый роутер
from .photo import photo_router
from .start import start_router

__all__ = ["start_router", "photo_router", "common_router"]
