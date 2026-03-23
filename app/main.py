import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from handlers.register import router as register
from handlers.admin import router as admin
from handlers.query import router as query

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def main():
    logging.basicConfig(level=logging.INFO)

    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # router ulash
    dp.include_router(register)
    dp.include_router(admin)
    dp.include_router(query)

    print("Bot ishga tushdi...")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())