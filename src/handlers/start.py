from aiogram import Router, types
from aiogram.filters import Command

start_router = Router()


@start_router.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    welcome_text = (
        "🤖 <b>Специализированный бот для удаления фона с фото людей</b>\n\n"
        "✅ <b>Что обрабатываю хорошо:</b>\n"
        "• Фотографии людей (лица, фигуры)\n"
        "• Четкие изображения с контрастным фоном\n"
        "• Портреты и селфи\n\n"
        "❌ <b>Что может не сработать:</b>\n"
        "• Животные, предметы, пейзажи\n"
        "• Размытые или темные фото\n"
        "• Сложные фоны (листва, узоры)\n\n"
        "📸 <b>Отправьте фото с человеком:</b>\n\n"
        "👇👇👇"  # ← Увеличили эмодзи в 2 раза!
    )
    await message.answer(
        welcome_text,
        parse_mode="HTML",  # использовать HTML-теги для красивого оформления:
        # <b>текст</b> - жирный
        # <i>текст</i> - курсив
        # <code>текст</code> - моноширинный
        # <a href="url">текст</a> - ссылка
        # reply_markup=get_main_keyboard() # Клавиатура под сообщением Добавляет кнопки для удобства пользователя
    )
