from aiogram import types, Router
from aiogram.filters import CommandStart

router = Router()
@router.message(CommandStart())
async def start_command(message: types.KeyboardButton):
    await message.answer("Salom! Men Telegram botman. Sizga qanday yordam bera olaman?")
    