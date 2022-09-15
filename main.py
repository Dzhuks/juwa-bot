# Импортируем необходимые классы.
import logging

from telegram.ext import Updater, CommandHandler

from config import App

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def start_command(update, context):
    username = f"{update.message.chat.first_name} {update.message.chat.last_name}"
    update.message.reply_text(f"""
    Сәлем, {username}!\nМен ювениалды бот-консультантпын!\n\nҚызықтыратын категорияға басып, сонда тақырыпты тандап, өз құқықтарын біл.
""")


def help_command(update, context):
    pass


def main():
    updater = Updater(App.config("BOT_TOKEN"))

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
