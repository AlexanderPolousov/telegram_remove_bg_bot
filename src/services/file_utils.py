import os
import uuid
from datetime import datetime


def ensure_directories_exist():
    """Создает необходимые директории для хранения файлов"""
    directories = ["data/input_images", "data/output_images"]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)


def generate_unique_filename(extension: str = "png") -> str:
    """Генерирует уникальное имя файла на основе времени и UUID"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    unique_id = str(uuid.uuid4())[:8]
    return f"{timestamp}_{unique_id}.{extension}"


def get_input_image_path(filename: str) -> str:
    """Возвращает полный путь к входному изображению"""
    return f"data/input_images/{filename}"


def get_output_image_path(filename: str) -> str:
    """Возвращает полный путь к выходному изображению"""
    return f"data/output_images/{filename}"
