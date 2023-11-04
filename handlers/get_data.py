from aiogram import types

from bot import dp
from db import Message, Session


@dp.message_handler(commands=['retrieve'])
async def retrieve_messages(message: types.Message):
    session = Session()

    messages = session.query(Message).filter(
        Message.chat_id == message.chat.id).all()

    if messages:
        response = "Messages in the database:\n"
        for msg in messages:
            response += f"{msg.user_id} {msg.created_at}: {msg.text}\n"
    else:
        response = "No messages found in the database."

    await message.reply(response)
