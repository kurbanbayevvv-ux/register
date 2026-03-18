from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def help_handler(message: Message):
    await message.answer("Botdan foydalanish uchun /start bosing")