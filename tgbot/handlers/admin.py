from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.services.db_api.db_command import BotDB

BotDB = BotDB('users_log.db')
async def admin_start(message: Message):
    await message.answer(f"Hello {message.chat.first_name}, you is admin!")

async def count_usr(message: Message):
    await message.answer(BotDB.count_users())

async def all_usr(message: Message):
    for i in BotDB.all_db():
        await message.answer(f'id: {i[0]}, name: {i[2]}, join: {i[3].split(" ")[0]}')


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
    dp.register_message_handler(count_usr, text="count", state="*", is_admin=True)
    dp.register_message_handler(all_usr, text="data", state="*", is_admin=True)
