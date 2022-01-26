from aiogram import types

from app.bot.forms import LanguageForm
from app.bot.forms import start_language_form_callback
from app.bot.middlewares import i18n
from app.database.models import User

_ = i18n.gettext

welcome_text = _("""👋 Велком!
У тебя как и у меня есть проблема с тем, что ты забываешь прочесть сохранённые в закладках статьи?
Бот поможет! (надеюсь, потому что мне помог) 
Он будет каждый день отправлять тебе по ссылочке на прочтение.

Как это работает:
* Ты отправляешь боту любую ссылку
* Ждешь пока наступит время рассылки
* Читаешь свою статью и помечаешь ее прочитанной у бота (под ссылкой будет кнопочка)
* Радуешься своей продуктивности!

Появилось желание прочесть что-то из добавленных ссылок, но не хочешь ждать наступления времени рассылки?
Используй команду /random :)
""")


async def send_welcome(message: types.Message):
    await User.get_from_message(message)
    await message.reply(_(welcome_text))
    await LanguageForm.start(start_language_form_callback)
