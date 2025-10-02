import os

from aiogram import F, Router
from aiogram.types import BufferedInputFile, Message

from src.services import (
    ensure_directories_exist,
    generate_unique_filename,
    get_input_image_path,
    get_output_image_path,
    image_processor,
)

photo_router = Router()


@photo_router.message(F.photo)
async def handle_photo(message: Message):
    """Обработчик фотографий"""
    try:
        # Создаем директории если их нет
        ensure_directories_exist()

        # Получаем фото наибольшего качества
        photo = message.photo[-1]
        file_id = photo.file_id
        file = await message.bot.get_file(file_id)
        file_path = file.file_path

        # Генерируем уникальное имя файла
        input_filename = generate_unique_filename()
        output_filename = generate_unique_filename()

        input_path = get_input_image_path(input_filename)
        output_path = get_output_image_path(output_filename)

        # Скачиваем фото
        await message.bot.download_file(file_path, input_path)

        # Обрабатываем изображение
        await image_processor.remove_background(input_path, output_path)

        # Отправляем обработанное изображение
        with open(output_path, "rb") as photo_file:
            await message.answer_photo(
                photo=BufferedInputFile(photo_file.read(), filename=output_filename),
                caption="Обработанное изображение",
            )

        # Очищаем временные файлы (опционально)
        os.remove(input_path)
        os.remove(output_path)

    except Exception as e:
        await message.answer(f"Произошла ошибка при обработке изображения: {str(e)}")
