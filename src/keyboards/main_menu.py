from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def get_main_keyboard():
    """Создает основную клавиатуру"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📸 Сделать фото"),
                KeyboardButton(text="📁 Загрузить фото"),
            ],
            [KeyboardButton(text="❓ Помощь"), KeyboardButton(text="🔄 Начать заново")],
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите действие или отправьте фото...",
    )
