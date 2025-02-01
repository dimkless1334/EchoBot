from aiogram.utils.keyboard import ReplyKeyboardBuilder

def info_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Информация")
    return builder.as_markup(resize_keyboard=True)