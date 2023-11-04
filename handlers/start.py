import logging

from aiogram import types

from bot import dp
from db import Message, Session


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text
    created_at = message.date

    # Create a new message object
    new_message = Message(chat_id=chat_id, user_id=user_id,
                          text=text, created_at=created_at)

    # Add the message to the database
    session = Session()
    session.add(new_message)
    session.commit()
    session.close()

    await message.reply("Message stored in the database.")
