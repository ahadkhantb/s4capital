from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
import asyncio
import logging

TOKEN = "7702859196:AAG2Rh9OW0twBmZ3nQo3a02cknPfPXu7Xf4"
ADMIN_ID = "@technicalahadyt"

bot = Bot(7702859196:AAG2Rh9OW0twBmZ3nQo3a02cknPfPXu7Xf4)
dp = Dispatcher(bot)

# Start Command
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user_id = message.from_user.id
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("💰 Earn Coins", callback_data='earn'))
    keyboard.add(InlineKeyboardButton("👥 Refer & Earn", callback_data='refer'))
    keyboard.add(InlineKeyboardButton("📤 Withdraw", callback_data='withdraw'))
    await message.reply("Welcome to Task Bot!", reply_markup=keyboard)

# Callback Handler
@dp.callback_query_handler(lambda call: True)
async def callback_handler(call: types.CallbackQuery):
    if call.data == "earn":
        await call.message.answer("Complete tasks & earn!")
    elif call.data == "refer":
        await call.message.answer(f"Invite friends & earn! Your referral link: https://t.me/s4capitalsearn_bot?start={call.from_user.id}")
    elif call.data == "withdraw":
        await call.message.answer("Withdraw system (Manual bKash)")
    await call.answer()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
