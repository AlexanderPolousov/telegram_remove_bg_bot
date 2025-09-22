from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    welcome_text = (
        "🎨 Добро пожаловать в Background Remover Bot!\n\n"
        "📸 Отправьте мне фото, и я удалю c него фон\n"
        "⚡ Результат вы получите в виде PNG-файла\n\n"
        "Просто отправьте фото или картинку 👇"
    )
    await message.answer(welcome_text)
