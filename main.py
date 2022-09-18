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
        f"Сәлем, {bold(username)}!\n",
        f"Мен ювенальды бот-консультантпын! Бастау үшін /cl командасын терініз немесе оған басыңыз.\n",
        f"/help - бот қолдану туралы көмек алу",
        f"/lang - қолданылатын тілді ауыстыру\n",
        f"Бот құқықтар туралы барлық ақпаратты ресми заңды құжаттардан алады және оны қарапайым, әрі түсінікті тілде түсіндіреді.",
        "Барлық дереккөздерге сілтемелер хабарламаның соңында болады.",
        sep='\n'
    )
    await message.reply(
        start_message,
        parse_mode=aiogram.types.ParseMode.MARKDOWN
    )


@dp.message_handler(commands=['about'])
async def about_command(message: types.Message):
    pass


@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    help_message = text(
        f"{bold('Құқық')} - мемлекет орнатқан және оның күшімен қорғалатын, жалпыға бірдей қоғамдық қатынастарды реттейтін тәртіп ережелерінің ( нормалардың ) жиынтығы.\n",
        "Оған жеке бастың құпиясын сақтау құқығы, өмір сүру құқығы, некеге тұрған азаматтардың құқықтары және тағыда басқалар жатады.\n",
        f"{bold('Ботты қалай қолдану:')}",
        "1. /cl командасын теру",
        "2. Аталған категориялар ішінен біреуін таңдаңыз",
        "3. Шыққан тақырыптарын ішінен біреуін тандап, өз құқықтарынызды зерттеніз\n",
        "Командалар:",
        "/about - бот туралы жалпы ақпарат шығару",
        "/lang - қолданылатын тілді ауыстыру",
        "/cl - бала құқықтар категорияларын шығару",
        sep="\n"
    )
    await message.reply(help_message, parse_mode=aiogram.types.ParseMode.MARKDOWN)


@dp.message_handler(commands=['lang'])
async def lang_command(message: types.Message):
    pass


# выводить все категории
@dp.message_handler(commands=['cl'])
async def clause_command(message: types.Message):
    await message.reply("Аталған категориялар ішінен біреуін таңданыз", reply_markup=kb.inline_kb1)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()
