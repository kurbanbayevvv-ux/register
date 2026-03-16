from aiogram import Router, types
from aiogram.filters import Command

router = Router()

@router.message(Command('help'))
async def help_cmd(message: types.Message):
    await message.answer("Yordam kerak bo'lsa\nShu yerda yozib keting!")

