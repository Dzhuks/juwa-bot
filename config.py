import os


class Config:
    __conf = {
        "BOT_TOKEN": os.getenv("BOT_TOKEN"),
        "lang": "kz",
        "age": ""
    }
    __setters = ["lang", "age"]

    @staticmethod
    def get(name):
        return Config.__conf[name]

    @staticmethod
    def set(name, value):
        if name not in Config.__setters:
            raise NameError("Name not accepted in set() method")
        Config.__conf[name] = value
