import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from db import create_pool, create_table, save_message
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.environ.get("BOT_TOKEN"))
dp = Dispatcher()
pool = None

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Salom! Men echo botman. Yozing, qaytaraman!")

@dp.message()
async def echo(message: types.Message):
    await save_message(
        pool,
        message.from_user.id,
        message.from_user.username,
        message.text
    )
    await message.answer(f"Echo: {message.text}")

async def main():
    global pool
    pool = await create_pool()
    await create_table(pool)
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
