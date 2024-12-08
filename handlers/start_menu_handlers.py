from aiogram import types, Router
from aiogram.filters import Command
import keyboards.main_keyboards as kbs
router = Router()


@router.message(Command("start"))
async def cmd_start(message: types.Message):
    print(f"user {message.from_user.first_name} call start_handler\n"
          f"message id: {message.message_id}")
    await message.reply(f"Привет {message.from_user.first_name}\n"
                        f"это оффициальный телеграм бот\n"
                        f"компании ОсОО Презент", reply_markup=kbs.main_kb)

