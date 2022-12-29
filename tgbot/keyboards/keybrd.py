from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Скидки USA🇺🇸'),
            KeyboardButton(text='Скидки PL🇵🇱'),
            KeyboardButton(text='Скидки UK🇬🇧'),
        ],
        [
            KeyboardButton(text=f'Поиск')
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
        ],
        [
            KeyboardButton(text='10 новых скидок'),
            KeyboardButton(text='Полный список скидок'),
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]
    ],
    resize_keyboard=True
)


admin_kb = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=f'Count')
        ],
        [
            KeyboardButton(text=f'Data')
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]
    ],
    resize_keyboard=True
)


anyway = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=f'Все равно показать'),
            KeyboardButton(text=f'Напишу по-другому')
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]
    ],
    resize_keyboard=True
)

reset = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text=f'В начало'),
        ],
        [
            KeyboardButton(text=f'Отмена')
        ]
    ],
    resize_keyboard=True
)