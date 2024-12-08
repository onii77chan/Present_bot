import asyncio
from aiogram import Bot, Dispatcher
from decouple import config
from handlers.start_menu_handlers import router as start_menu_handler


TOKEN = config('TOKEN')
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def on_startup():

    # routers
    dp.include_router(start_menu_handler)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(on_startup())
