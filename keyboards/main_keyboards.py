from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup,

)

main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Зарегистрироваться"), KeyboardButton(text="Войти")],
        [KeyboardButton(text="Акции")],
    ],
    resize_keyboard=True,
)

contacts_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Telegram чат", url="https://t.me/presentsweets")],
        [InlineKeyboardButton(text="Whatsapp чат", url="https://t.me/presentsweets")],
        [InlineKeyboardButton(text="Телефон номер", url="https://t.me/presentsweets")],
    ],
)

settings_kb = InlineKeyboardMarkup(
    inline_keyboard=[]
)
