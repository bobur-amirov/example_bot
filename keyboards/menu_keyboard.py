from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Menu 1"),
            KeyboardButton(text="Menu 2"),
        ],
    ],
    resize_keyboard=True
)
