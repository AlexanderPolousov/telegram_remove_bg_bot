import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from src.handlers import common_router, photo_router, start_router
from src.utils.logger import setup_logging

# Загружаем переменные окружения
load_dotenv()


async def main():
    # Настраиваем цветное логирование ДО создания бота
    setup_logging()

    # Создаем бота и диспетчера
    bot = Bot(token=os.getenv("BOT_TOKEN"))
    dp = Dispatcher()

    # Подключаем роутеры
    dp.include_router(start_router)
    dp.include_router(common_router)
    dp.include_router(photo_router)

    # Теперь используем logging вместо print
    logging.info("🤖 БОТ ЗАПУЩЕН И ГОТОВ K РАБОТЕ!")
    logging.info("✅ Все роутеры подключены")
    logging.info("🚀 Бот начал прослушивание сообщений...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
