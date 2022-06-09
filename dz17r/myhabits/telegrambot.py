from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os

from flask_login import current_user

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)
from models import Register

@dp.message_handler()
async def echo_send(message : types.message):
    form_email = message.text
    try:
        check_user = Register.query.filter_by(email=form_email).first()

        list = (check_user.nickname,
                check_user.name,
                check_user.surname,
                check_user.colour,
                check_user.telegram
                )

        if message.text == form_email:
            await message.answer(f'Hi: {list}!')
    except:
        await message.answer('Sorry, nothing in database!')
    # await bot.send_message(message.from_user.id, 'Hello world')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True)