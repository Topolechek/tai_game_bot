from aiogram import Dispatcher
from aiogram.types import Message
from tgbot.keyboards.keybrd import admin_kb
from tgbot.services.db_api.db_command import BotDB

BotDB = BotDB('users_log.db')


async def admin_actions(message: Message):
    await message.answer(f"Admin menu for {message.chat.first_name}", reply_markup=admin_kb)


async def count_usr(message: Message):
    await message.answer(BotDB.count_users())


async def all_usr(message: Message):
    for i in BotDB.all_db():
        await message.answer(f'id: {i[0]}, name: {i[2]}, join: {i[3].split(" ")[0]}',
                             disable_notification=True)


def register_admin(dp: Dispatcher):
    # admin menu
    dp.register_message_handler(admin_actions, text="admin", state="*", is_admin=True)
    dp.register_message_handler(count_usr, text="Count", state="*", is_admin=True)
    dp.register_message_handler(all_usr, text="Data", state="*", is_admin=True)
