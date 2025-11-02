import asyncio
import logging
import wikipedia
from aiogram import Bot, Dispatcher, types, Router
from aiogram.filters import Command
from aiogram.types import Message

API_TOKEN = "TOKEN" #token yoz ozinikini
logging.basicConfig(level=logging.INFO)

wikipedia.set_lang("uz")  # tilni o'zgartir

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Salom! Men Wikipedia Botman \nMenga istalgan so‘zni yozing, men sizga ma’lumot topaman!")

@router.message()
async def wiki_search(message: Message):
    query = message.text
    try:
        result = wikipedia.summary(query, sentences=3)
        await message.answer(result)
    except wikipedia.exceptions.DisambiguationError as e:
        await message.answer(f"Bu so‘z bir nechta ma’noga ega. Iltimos, aniqroq yozing\nMasalan: {e.options[:5]}")
    except wikipedia.exceptions.PageError:
        await message.answer("Kechirasiz, bu mavzu bo‘yicha ma’lumot topilmadi")
    except Exception as e:
        await message.answer("Xatolik yuz berdi. Keyinroq urinib ko‘ring")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
