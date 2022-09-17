# Импортируем необходимые классы.
import logging

from config import Config

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def start_command(update, context):
    username = "fjdk"
    f"""
        Сәлем, {username}!\nМен ювениалды бот-консультантпын!\n\nҚызықтыратын категорияға басып, сонда тақырыпты тандап, өз құқықтарын біл.
    """
    pass


def help_command(update, context):
    pass


def main():
    pass


if __name__ == '__main__':
    config = Config()
    print(config.get("BOT_TOKEN"))
    # main(
