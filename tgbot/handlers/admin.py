from aiogram import Dispatcher
from aiogram.types import Message


async def admin_start(message: Message):
    await message.reply(f"Hello {message.chat.first_name}, you is admin!")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)