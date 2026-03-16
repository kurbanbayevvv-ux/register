from aiogram import Router, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
router = Router()

menu_inline = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Google", url="https://www.google.com"),
        InlineKeyboardButton(text="YouTube", url="https://www.youtube.com")
    ],
    [
        InlineKeyboardButton(text="Telegram", url="https://www.telegram.org")
    ]
])