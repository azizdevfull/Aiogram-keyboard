from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


some_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-tugma"),
            KeyboardButton(text="2-tugma"),
            KeyboardButton(text="3-tugma")
        ],
        [
            KeyboardButton(text="4-tugma"),
            KeyboardButton(text="5-tugma"),
            KeyboardButton(text="6-tugma")
        ],
    ],
    resize_keyboard=True
) 