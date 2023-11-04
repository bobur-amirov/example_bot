from aiogram.dispatcher.filters import Command
from aiogram.types import Message
from keyboards.menu_keyboard import menu


from bot import dp


@dp.message_handler(Command("menu"))
async def menu_handler(message: Message):
    await message.answer("Menyuni tanlang", reply_markup=menu)
