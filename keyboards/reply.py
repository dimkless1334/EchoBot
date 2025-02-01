from aiogram.utils.keyboard import ReplyKeyboardBuilder


bot_info_button = {
    "text" : "О боте"
}

user_info_button = {
    "text" : "Информация о пользователе"
}

contacts_button = {
    "text" : "Контакты"
}

statistics_button = {
    "text": "Статистика"
}

def create_reply_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.button(text=bot_info_button["text"])
    builder.button(text=user_info_button["text"])
    builder.button(text=contacts_button["text"])
    builder.button(text=statistics_button["text"])

    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)

