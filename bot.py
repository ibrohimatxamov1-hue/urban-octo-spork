import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
import os

# .env fayldan tokenni yuklaymiz
load_dotenv(r"C:\Users\ЧеловеК\Desktop\mybot\.env")
TOKEN = os.getenv("BOT_TOKEN")

# Bot va Dispatcher obyektlarini yaratamiz
bot = Bot(token=TOKEN)
dp = Dispatcher()

# /start komandasi uchun handler
@dp.message(Command("start"))
async def start_cmd(message: Message):
    user_id = message.from_user.id
    ref_link = f"https://t.me/konkursmusabiy_bot?start={user_id}"

    text = (
        f"👋 Salom, {message.from_user.first_name}!\n\n"
        f"Do‘stlaringizni taklif qiling!\n"
        f"4 ta do‘stingizni taklif qiling va konkurs ishtirokchisi bo‘ling 🎁\n\n"
        f"🔗 Sizning referal linkingiz:\n{ref_link}"
    )

    await message.answer(text)

# Botni ishga tushiramiz
async def main():
    print("✅ Bot ishga tushdi, Telegramda /start yozing!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
