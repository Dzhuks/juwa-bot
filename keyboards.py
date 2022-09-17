from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton


button_clause1 = KeyboardButton("Какая-та статья")
clause_kb = ReplyKeyboardMarkup(resize_keyboard=True)
clause_kb.add(button_clause1)

inline_btn_1 = InlineKeyboardButton('Баланың жеке құқықтары', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
