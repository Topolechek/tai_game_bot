from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.keyboards.keybrd import kb_menu, us_menu, pl_menu, uk_menu
from tgbot.misc import Level
from tgbot.services.parser import all_games_reg

# region mostwanted most_pop
us = 'https://psprices.com/region-us/collection/most-wanted-deals?platform=Switch'
pl = 'https://psprices.com/region-pl/collection/most-wanted-deals?platform=Switch'
uk = 'https://psprices.com/region-gb/collection/most-wanted-deals?platform=Switch'

# region lower prices most_sale
uslp = 'https://psprices.com/region-us/collection/lowest-prices-ever?platform=Switch'
pllp = 'https://psprices.com/region-pl/collection/lowest-prices-ever?platform=Switch'
uklp = 'https://psprices.com/region-gb/collection/lowest-prices-ever?platform=Switch'


# start/cancel
async def user_start(message: Message):
    await message.answer(f"Привет {message.chat.first_name}!", reply_markup=kb_menu)
    await Level.region.set()


async def user_cancel(message: Message, state: FSMContext):
    await message.answer(f"Выбирай категорию", reply_markup=kb_menu,
                         disable_notification=True)
    await state.reset_state()


# choise region
async def us_menu_sale(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_region'] = answer
    await message.answer(f"Выбери категорию", reply_markup=us_menu)
    await Level.category.set()


async def pl_menu_sale(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_region'] = answer
    await message.answer(f"Выбери категорию", reply_markup=pl_menu)
    await Level.category.set()


async def uk_menu_sale(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_region'] = answer
    await message.answer(f"Выбери категорию", reply_markup=uk_menu)
    await Level.category.set()


# choise_category_us
async def user_us_most_sale_10(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_category'] = answer
    game = all_games_reg(uslp)
    for i in game[:10]:
        await message.answer(f'[{i[0]}]'
                             f'({i[3]})' + '\n'
                                           f'{"🔥" if int(i[1]) > 50 else ""}Скидка: [{i[1]}] %' + '\n'
                                                                                                   f'Цена сейчас: $[{i[2]}]' + '\n'
                                                                                                                               f'[Купить]'
                                                                                                                               f'({i[4]})',
                             parse_mode='Markdown',
                             disable_notification=True)
    await state.reset_state()


async def user_us_most_pop_10(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_category'] = answer
    game = all_games_reg(us)
    for i in game[:10]:
        await message.answer(f'[{i[0]}]'
                             f'({i[3]})' + '\n'
                                           f'{"🔥" if int(i[1]) > 50 else ""}Скидка: [{i[1]}] %' + '\n'
                                                                                                   f'Цена сейчас: $[{i[2]}]' + '\n'
                                                                                                                               f'[Купить]'
                                                                                                                               f'({i[4]})',
                             parse_mode='Markdown',
                             disable_notification=True)
    await state.reset_state()


async def user_us_sale_all(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_category'] = answer
    game = all_games_reg(us)
    for i in game:
        await message.answer(f'[{i[0]}]'
                             f'({i[3]})' + '\n'
                                           f'{"🔥" if int(i[1]) > 50 else ""}Скидка: [{i[1]}] %' + '\n'
                                                                                                   f'Цена сейчас: $[{i[2]}]' + '\n'
                                                                                                                               f'[Купить]'
                                                                                                                               f'({i[4]})',
                             parse_mode='Markdown',
                             disable_notification=True)
    await state.reset_state()


# choise_category_pl
async def user_pl_most_sale_10(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_category'] = answer
    game = all_games_reg(pllp)
    for i in game[:10]:
        await message.answer(f'[{i[0]}]'
                             f'({i[3]})' + '\n'
                                           f'{"🔥" if int(i[1]) > 50 else ""}Скидка: [{i[1]}] %' + '\n'
                                                                                                   f'Цена сейчас: zł[{i[2]}]' + '\n'
                                                                                                                                f'[Купить]'
                                                                                                                                f'({i[4]})',
                             parse_mode='Markdown',
                             disable_notification=True)
    await state.reset_state()


async def user_pl_most_pop_10(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_category'] = answer
    game = all_games_reg(pl)
    for i in game[:10]:
        await message.answer(f'[{i[0]}]'
                             f'({i[3]})' + '\n'
                                           f'{"🔥" if int(i[1]) > 50 else ""}Скидка: [{i[1]}] %' + '\n'
                                                                                                   f'Цена сейчас: zł[{i[2]}]' + '\n'
                                                                                                                                f'[Купить]'
                                                                                                                                f'({i[4]})',
                             parse_mode='Markdown',
                             disable_notification=True)
    await state.reset_state()


async def user_pl_sale_all(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_category'] = answer
    game = all_games_reg(pl)
    for i in game:
        await message.answer(f'[{i[0]}]'
                             f'({i[3]})' + '\n'
                                           f'{"🔥" if int(i[1]) > 50 else ""}Скидка: [{i[1]}] %' + '\n'
                                                                                                   f'Цена сейчас: zł[{i[2]}]' + '\n'
                                                                                                                                f'[Купить]'
                                                                                                                                f'({i[4]})',
                             parse_mode='Markdown',
                             disable_notification=True)
    await state.reset_state()


# choise_category_uk
async def user_uk_most_sale_10(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_category'] = answer
    game = all_games_reg(uklp)
    for i in game[:10]:
        await message.answer(f'[{i[0]}]'
                             f'({i[3]})' + '\n'
                                           f'{"🔥" if int(i[1]) > 50 else ""}Скидка: [{i[1]}] %' + '\n'
                                                                                                   f'Цена сейчас: £[{i[2]}]' + '\n'
                                                                                                                               f'[Купить]'
                                                                                                                               f'({i[4]})',
                             parse_mode='Markdown',
                             disable_notification=True)
    await state.reset_state()


async def user_uk_most_pop_10(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_category'] = answer
    game = all_games_reg(uk)
    for i in game[:10]:
        await message.answer(f'[{i[0]}]'
                             f'({i[3]})' + '\n'
                                           f'{"🔥" if int(i[1]) > 50 else ""}Скидка: [{i[1]}] %' + '\n'
                                                                                                   f'Цена сейчас: £[{i[2]}]' + '\n'
                                                                                                                               f'[Купить]'
                                                                                                                               f'({i[4]})',
                             parse_mode='Markdown',
                             disable_notification=True)
    await state.reset_state()


async def user_uk_sale_all(message: Message, state: FSMContext):
    answer = message.text

    async with state.proxy() as data:
        data['answer_category'] = answer
    game = all_games_reg(uk)
    for i in game:
        await message.answer(f'[{i[0]}]'
                             f'({i[3]})' + '\n'
                                           f'{"🔥" if int(i[1]) > 50 else ""}Скидка: [{i[1]}] %' + '\n'
                                                                                                   f'Цена сейчас: £[{i[2]}]' + '\n'
                                                                                                                               f'[Купить]'
                                                                                                                               f'({i[4]})',
                             parse_mode='Markdown',
                             disable_notification=True)
    await state.reset_state()


def register_user(dp: Dispatcher):
    # base
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(user_cancel, text='Отмена', state="*")

    # first menu choise region
    dp.register_message_handler(us_menu_sale, text='Скидки USA🇺🇸', state="*")
    dp.register_message_handler(pl_menu_sale, text='Скидки PL🇵🇱', state="*")
    dp.register_message_handler(uk_menu_sale, text='Скидки UK🇬🇧', state="*")

    # second menu choise category
    # us
    dp.register_message_handler(user_us_most_sale_10, text='10 дешевле чем когда либо us', state=Level.category)
    dp.register_message_handler(user_us_most_pop_10, text='10 самых популярных us', state=Level.category)
    dp.register_message_handler(user_us_sale_all, text='Полный список скидок us', state=Level.category)

    # pl
    dp.register_message_handler(user_pl_most_sale_10, text='10 дешевле чем когда либо pl', state=Level.category)
    dp.register_message_handler(user_pl_most_pop_10, text='10 самых популярных pl', state=Level.category)
    dp.register_message_handler(user_pl_sale_all, text='Полный список скидок pl', state=Level.category)

    # uk
    dp.register_message_handler(user_uk_most_sale_10, text='10 дешевле чем когда либо uk', state=Level.category)
    dp.register_message_handler(user_uk_most_pop_10, text='10 самых популярных uk', state=Level.category)
    dp.register_message_handler(user_uk_sale_all, text='Полный список скидок uk', state=Level.category)

    dp.register_message_handler(user_cancel, text='Назад', state=Level.region)
    dp.register_message_handler(user_start, text='Назад', state=Level.category)
