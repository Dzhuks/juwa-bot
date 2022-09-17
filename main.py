import logging

import aiogram.types
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.markdown import bold, text

import keyboards as kb
from config import Config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

config = Config()
bot = Bot(token=config.get("BOT_TOKEN"))
dp = Dispatcher(bot)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Сіз баланың жеке құқықтары категориясын бастыныз',
                           reply_markup=kb.clause_kb)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    username = message.from_user.full_name
    start_message = text(
        f"Сәлем, {bold(username)}!",
        f"Мен ювениалды бот-консультантпын!\n",
        f"Қызықтыратын категорияға басып, сонда тақырыпты тандап, өз құқықтарын біл.\n",
        f"Егер тілді өзгерткін келсе, /setting командасына басып, қолайлы тілді таңдаңыз\n",
        f"Егер боттың жұмысына сұрақтар болса, /help командасына басыңыз.",
        sep='\n'
    )
    await message.reply(
        start_message,
        parse_mode=aiogram.types.ParseMode.MARKDOWN,
        reply_markup=kb.inline_kb1
    )


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    help_message = text(
        "Құқық - мемлекет орнатқан және оның күшімен қорғалатын, жалпыға бірдей қоғамдық қатынастарды реттейтін тәртіп ережелерінің ( нормалардың ) жиынтығы. Құқықтың түсініктері бірнеше, бірақ мазмұндары біреу-ақ.",
        "Оған жеке бастың құпиясын сақтау құқығы, өмір сүру құқығы, некеге тұрған азаматтардың құқықтары және тағыда басқалар жатады\n",
        "Командалар:",
        "/start - бот жұмыс жасауды бастайды",
        "/help - ботпен пайдаланушымен таныстыру",
        sep="\n"
    )
    await message.reply(help_message)


# выводить все категории
@dp.message_handler(commands=['cl'])
async def clause_command(message: types.Message):
    pass


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
