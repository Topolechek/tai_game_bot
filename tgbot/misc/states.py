from aiogram.dispatcher.filters.state import StatesGroup, State


class Level(StatesGroup):
    region = State()
    category = State()
    search = State()
    good_job = State()
