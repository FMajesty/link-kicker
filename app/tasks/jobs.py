from aiogram.utils import exceptions as aiogram_exceptions
from loguru import logger

from app.bot import bot
from app.bot.messages import get_random_link_message
from app.database.models import User
from app.misc.sentry import capture_exception


async def link_mailing():
    for user in await User.all():
        message_text, markup = await get_random_link_message(user, mailing=True)
        try:
            await bot.send_message(user.tg_id, message_text, reply_markup=markup)
        except aiogram_exceptions.BotBlocked:
            logger.info(f"{user.tg_id} blocked bot")
            await user.delete()
        except Exception as ex:  # noqa
            capture_exception(ex)
