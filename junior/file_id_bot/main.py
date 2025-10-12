from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Salom!\n"
        "Menga video, rasm yoki fayl yuboring — men sizga uning <b>file_id</b>’sini aytaman.",
        parse_mode="HTML"
    )

@dp.message(F.photo)
async def get_photo_id(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"🖼 Rasm file_id:\n<code>{file_id}</code>", parse_mode="HTML")

@dp.message(F.video)
async def get_video_id(message: Message):
    file_id = message.video.file_id
    await message.answer(f"🎬 Video file_id:\n<code>{file_id}</code>", parse_mode="HTML")

@dp.message(F.document)
async def get_doc_id(message: Message):
    file_id = message.document.file_id
    await message.answer(f"📄 Fayl file_id:\n<code>{file_id}</code>", parse_mode="HTML")

@dp.message(F.audio)
async def get_audio_id(message: Message):
    file_id = message.audio.file_id
    await message.answer(f"🎵 Audio file_id:\n<code>{file_id}</code>", parse_mode="HTML")

async def main():
    print("🤖 Bot ishga tushdi...")
    await dp.start_polling(bot)

from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
import os
from dotenv import load_dotenv

# 🔹 1. .env fayldan TOKEN o‘qish
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# 🔹 2. Token mavjudligini tekshirish
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN topilmadi! .env faylni tekshiring.")

# 🔹 3. Bot va Dispatcher obyektlari
bot = Bot(token=TOKEN)
dp = Dispatcher()


# ===================== HANDLERLAR ===================== #

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "👋 Salom!\n"
        "Menga video, rasm yoki fayl yuboring — men sizga uning <b>file_id</b>’sini aytaman.",
        parse_mode="HTML"
    )


@dp.message(F.photo)
async def get_photo_id(message: Message):
    file_id = message.photo[-1].file_id
    await message.answer(f"🖼 Rasm file_id:\n<code>{file_id}</code>", parse_mode="HTML")


@dp.message(F.video)
async def get_video_id(message: Message):
    file_id = message.video.file_id
    await message.answer(f"🎬 Video file_id:\n<code>{file_id}</code>", parse_mode="HTML")


@dp.message(F.document)
async def get_doc_id(message: Message):
    file_id = message.document.file_id
    await message.answer(f"📄 Fayl file_id:\n<code>{file_id}</code>", parse_mode="HTML")


@dp.message(F.audio)
async def get_audio_id(message: Message):
    file_id = message.audio.file_id
    await message.answer(f"🎵 Audio file_id:\n<code>{file_id}</code>", parse_mode="HTML")

async def main():
    print("🤖 Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
