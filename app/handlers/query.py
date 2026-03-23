from aiogram import F, Router, types
from database.postgres import getUsers, countUsers

router = Router()

@router.callback_query(F.data == 'users')
async def user_query_handler(callback: types.CallbackQuery):
    users = getUsers()
    response_text = ""
    for user in users:
        response_text += f"{user[1]} {user[2]}\n"
    await callback.message.answer("Foydalanuvchilar:     \n" + response_text)

@router.callback_query(F.data == 'count_users')
async def count_users_query_handler(callback: types.CallbackQuery):
    count_users = countUsers()
    await callback.message.answer(f"foydalanuvchilar soni: {count_users}")