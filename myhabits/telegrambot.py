from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import os
from __init__ import db
from models import Task, Habit

from flask_login import current_user

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot)
from models import User

@dp.message_handler()
async def echo_send(message : types.message):
    nickname = message.text
    try:
        check_user = User.query.filter_by(nickname=nickname).first()
        tasks = db.session.query(Task, Habit).join(Habit).all()
    
        for task, habit in tasks:
            name = habit.name
            description = habit.description
            wish = task.wish_period
            start = task.start_period

        if message.text == nickname:
            await message.answer(f'Hi: {name, description, wish, start, check_user.email}!')
    except:
        await message.answer('Sorry, nothing in database!')
    # await bot.send_message(message.from_user.id, 'Hello world')
    # await message.reply(message.text)
    # await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, skip_updates=True)