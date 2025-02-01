from aiogram.utils.keyboard import InlineKeyboardBuilder

git_hub_button = {
    "text":"GitHub", 
    "url":"https://github.com/dimkless1334"
}

telegram_button = {
    "text": "Telegram",
    "url": "https://t.me/Dimkless3034"
}

delete_button = {
    "text": "❌ Удалить",
    "callback_data": "delete"
}

def create_contacts_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text=git_hub_button["text"], url=git_hub_button["url"])
    builder.button(text=telegram_button["text"], url=telegram_button["url"])

    builder.adjust(2)

    return builder.as_markup()

def create_inline_keyboard():
    builder = InlineKeyboardBuilder()

    builder.button(text=delete_button["text"], callback_data=delete_button["callback_data"])
    
    builder.adjust(2,1)

    return builder.as_markup()

