from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_keyboard():
    """Создает основную клавиатуру"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📸 Сделать фото"),
                KeyboardButton(text="📁 Загрузить фото"),
            ],
            [KeyboardButton(text="❓ Помощь")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие...",
    )
