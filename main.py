import logging

import aiogram.types
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import bold

from config import Config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

config = Config()
bot = Bot(token=config.get("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    username = message.from_user.full_name
    await message.reply(
        f"Сәлем, {bold(username)}!\n"
        f"Мен ювениалды бот-консультантпын!\n\n"
        f"Қызықтыратын категорияға басып, сонда тақырыпты тандап, өз құқықтарын біл.\n\n"
        f"Егер тілді өзгерткін келсе, /setting командасына басып, қолайлы тілді таңда",
        parse_mode=aiogram.types.ParseMode.MARKDOWN
    )


@dp.message_handler(commands=['help'])
def help_command(update, context):
    pass


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
