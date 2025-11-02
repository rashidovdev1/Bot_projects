import requests
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "TOKEN_YOZ"
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def salom_ber(message: types.Message):
    await message.answer("Salom! Men sizga bugungi valyuta kurslarini aytama")

    url = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    data = requests.get(url).json()

    currencies = ["USD", "EUR", "GBP", "RUB"]

    text = "Bugungi valyuta kurslari:\n\n"
    for value in data:
        if value["Ccy"] in currencies:
            text += f"1 {value['CcyNm_UZ']} = {value['Rate']} so'm\n"

    await message.answer(text)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
