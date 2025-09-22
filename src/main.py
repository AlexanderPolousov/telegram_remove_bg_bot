import asyncio
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers.photo import photo_router
from handlers.start import start_router

# Загружаем переменные окружения
load_dotenv()

# Создаем бота и диспетчера
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(start_router)
dp.include_router(photo_router)


async def main():
    print("🤖 БОТ ЗАПУЩЕН И ГОТОВ K РАБОТЕ!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
