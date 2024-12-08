from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup,
    CallbackQuery,
)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="1 button"), KeyboardButton(text="2 button")],
        [KeyboardButton(text="3 button"), KeyboardButton(text="4 button")],
    ]
)
