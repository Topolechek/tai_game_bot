from datetime import datetime

from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.keyboards.keybrd import kb_menu, all_menu
from tgbot.misc import Level
from tgbot.services.db_api.db_command import BotDB
from tgbot.services.parser import all_games_reg

BotDB = BotDB('users_log.db')


# start/cancel
async def user_start(message: Message):
    if not BotDB.user_exists(message.chat.id):
        BotDB.add_user(message.chat.id, message.chat.first_name, datetime.now())
        print('awq')
    await message.answer(f"Привет {message.chat.first_name}!", reply_markup=kb_menu)
    await Level.region.set()

# choise region
async def us_menu_sale(message: Message, state: FSMContext):
    reg_ans = message.text
    await state.update_data(reg_ans=reg_ans)

    if reg_ans == 'Скидки USA🇺🇸':
        await message.answer(f"Выбери категорию", reply_markup=all_menu)
    elif reg_ans == 'Скидки PL🇵🇱':
        await message.answer(f"Выбери категорию", reply_markup=all_menu)
    elif reg_ans == 'Скидки UK🇬🇧':
        await message.answer(f"Выбери категорию", reply_markup=all_menu)

    await Level.category.set()


async def alls_games_ev(message: Message, state: FSMContext):
    addr = ''
    ess = ''
    coun = 0
    data = await state.get_data()
    reg_ans = data.get('reg_ans')
    cat_ans = message.text if message.text in ['10 дешевле чем когда либо', '10 самых популярных',
                                               'Полный список скидок'] else '10 дешевле чем когда либо'
    if reg_ans == 'Скидки USA🇺🇸':
        addr = 'https://psprices.com/region-us'
    if reg_ans == 'Скидки PL🇵🇱':
        addr = 'https://psprices.com/region-pl'
    if reg_ans == 'Скидки UK🇬🇧':
        addr = 'https://psprices.com/region-gb'

    if cat_ans == '10 дешевле чем когда либо':
        ess = '/collection/lowest-prices-ever?platform=Switch'
        coun = 10
    if cat_ans == '10 самых популярных':
        ess = '/collection/most-wanted-deals?platform=Switch'
        coun = 10
    if cat_ans == 'Полный список скидок':
        ess = '/collection/lowest-prices-ever?platform=Switch'
        coun = 36

    sit = addr + ess
    game = all_games_reg(sit)
    for i in game[:coun]:
        name = i[0]
        disc = i[1]
        price = i[2]
        imag = i[3]
        site = i[4]
        valut = {'Скидки USA🇺🇸': '$', 'Скидки PL🇵🇱': 'zł', 'Скидки UK🇬🇧': '£'}
        await message.answer(f'[{name}]'
                             f'({imag})' + '\n'
                                           f'{"🔥" if (int(disc) > 50) else ""}Скидка: [{disc}] %' + '\n'
                                                                                                                                                      f'Цена сейчас: {valut[reg_ans]}[{price}]' + '\n'
                                                                                                                                                                                                  f'[Купить]'
                                                                                                                                                                                                  f'({site})',
                             parse_mode='Markdown',
                             disable_notification=True)

        await state.update_data(cat_ans=None)


def register_user(dp: Dispatcher):
    # base
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_start, text='Отмена', state="*")

    # first menu choise region
    dp.register_message_handler(us_menu_sale, text='Скидки USA🇺🇸', state=Level.region)
    dp.register_message_handler(us_menu_sale, text='Скидки PL🇵🇱', state=Level.region)
    dp.register_message_handler(us_menu_sale, text='Скидки UK🇬🇧', state=Level.region)

    dp.register_message_handler(alls_games_ev, state=Level.category)
