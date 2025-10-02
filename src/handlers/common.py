from aiogram import Router, types
from aiogram.filters import Command

from src.handlers.start import get_start_text
from src.keyboards.main_menu import get_main_keyboard

common_router = Router()


@common_router.message(lambda message: message.text == "❓ Помощь")
async def help_button(message: types.Message):
    """Обработчик кнопки Помощь"""
    help_text = (
        "ℹ️ <b>Инструкция по использованию бота:</b>\n\n"
        "📸 <b>Как работать с ботом:</b>\n"
        "• Отправьте фото человека\n"
        "• Дождитесь обработки (10-30 секунд)\n"
        "• Получите результат без фона\n\n"
        "🖼️ <b>Рекомендации по фото:</b>\n"
        "• Четкое изображение с хорошим освещением\n"
        "• Контраст между человеком и фоном\n"
        "• Минимальные тени и отражения\n\n"
        "📎 <b>Просто отправьте фото - и бот сделает всё сам!</b>"
    )
    await message.answer(help_text, parse_mode="HTML", reply_markup=get_main_keyboard())


@common_router.message(lambda message: message.text == "📸 Сделать фото")
async def take_photo_button(message: types.Message):
    """Обработчик кнопки Сделать фото"""
    await message.answer(
        "📱 <b>Как сделать фото:</b>\n\n"
        "1. Нажмите на значок 📎 (скрепка) в поле ввода\n"
        '2. Выберите "Камера" 📸\n'
        "3. Сделайте фото человека\n"
        "4. Отправьте фото - бот автоматически удалит фон!\n\n"
        "<i>Фото должно быть четким с хорошо видимым человеком</i>",
        parse_mode="HTML",
        reply_markup=get_main_keyboard(),
    )


@common_router.message(lambda message: message.text == "📁 Загрузить фото")
async def upload_photo_button(message: types.Message):
    """Обработчик кнопки Загрузить фото"""
    await message.answer(
        "📂 <b>Как загрузить фото:</b>\n\n"
        "1. Нажмите на значок 📎 (скрепка) в поле ввода\n"
        '2. Выберите "Галерея" или "Фото"\n'
        "3. Выберите фото с человеком из вашей галереи\n"
        "4. Отправьте фото - фон будет удален автоматически!\n\n"
        "<i>Рекомендуем выбирать фото с контрастным фоном</i>",
        parse_mode="HTML",
        reply_markup=get_main_keyboard(),
    )


@common_router.message(Command("help"))
async def help_command(message: types.Message):
    """Обработчик команды /help"""
    await help_button(message)


@common_router.message(lambda message: message.text == "🔄 Начать заново")
async def restart_button(message: types.Message):
    """Обработчик кнопки Начать заново"""
    await message.answer(
        get_start_text(), parse_mode="HTML", reply_markup=get_main_keyboard()
    )
