from aiogram import types, Router
from aiogram.filters import command, Command
import keyboards.main_keyboards as main_keyboard
import keyboards.main_keyboards as kbs
router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.reply(f"Привет {message.from_user.first_name}", reply_markup=kbs.main_kb)


@router.message(Command("catalog"))
async def catalog(message: types.Message):
    await message.answer("apppppp")
