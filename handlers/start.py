import logging

from aiogram import types

from bot import dp
from db import Message, Session


@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    session = Session()
    chat_id = message.chat.id
    user_id = message.from_user.id
    text = message.text
    created_at = message.date

    user = session.query(Message).filter(Message.user_id == user_id).first()
    if not user:

        # Create a new message object
        new_message = Message(chat_id=chat_id, user_id=user_id,
                              text=text, created_at=created_at)

    # Add the message to the database
        session.add(new_message)
        session.commit()
        session.close()

        await message.reply("Message stored in the database.")
    await message.reply("Assalomu alaykum")
