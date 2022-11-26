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


us_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='10 дешевле чем когда либо us'),
            KeyboardButton(text='10 самых популярных us'),
            KeyboardButton(text='Полный список скидок us'),
        ],
        [
            KeyboardButton(text=f'Отмена'),
            KeyboardButton(text=f'Назад')
        ]
    ],
    resize_keyboard=True
)

pl_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='10 дешевле чем когда либо pl'),
            KeyboardButton(text='10 самых популярных pl'),
            KeyboardButton(text='Полный список скидок pl'),
        ],
        [
            KeyboardButton(text=f'Отмена'),
            KeyboardButton(text=f'Назад')
        ]
    ],
    resize_keyboard=True
)

uk_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='10 дешевле чем когда либо uk'),
            KeyboardButton(text='10 самых популярных uk'),
            KeyboardButton(text='Полный список скидок uk'),
        ],
        [
            KeyboardButton(text=f'Отмена'),
            KeyboardButton(text=f'Назад')
        ]
    ],
    resize_keyboard=True
)