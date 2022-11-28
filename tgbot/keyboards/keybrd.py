from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Скидки USA🇺🇸'),
            KeyboardButton(text='Скидки PL🇵🇱'),
            KeyboardButton(text='Скидки UK🇬🇧'),
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]
    ],
    resize_keyboard=True
)


all_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='10 дешевле чем когда либо'),
            KeyboardButton(text='10 самых популярных'),
            KeyboardButton(text='Полный список скидок'),
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]
    ],
    resize_keyboard=True
)

