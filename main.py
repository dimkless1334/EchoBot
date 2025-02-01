import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from dotenv import load_dotenv
# Импортируем обработчики из папки handlers
from handlers.user import user_router

# Загружаем переменные из .env
load_dotenv()

# Инициализация бота и диспетчера
TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Регистрируем роутер
dp.include_router(user_router)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        import asyncio
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот отключен!")