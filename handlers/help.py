from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from bot import dp


@dp.message_handler(CommandHelp())
async def help_handler(message: types.Message):

    await message.answer("Sizga qanday yordam kerak")
