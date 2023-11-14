import asyncio
from aiogram import types

from bot import dp
from db import Message, Session


@dp.message_handler()
async def echo(message: types.Message):
    session = Session()
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text
    created_at = message.date

    user = session.query(Message).filter(Message.user_id == user_id).first()
    if not user:

        # mm = await message.reply("avval strat bosing")
        service_message = await message.reply("Xabar 5 sekunddan so'ng o'chib ketadi.")
        # 5 sekun kutib xabarlarni o'chirib tashlaymiz
        await asyncio.sleep(5)
        await message.delete()
        await service_message.delete()
        # await message.delete()
        # await mm.delete()
