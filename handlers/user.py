from aiogram import Router, F
from aiogram.types import Message
from keyboards.reply import info_keyboard
from keyboards.inline import create_inline_keyboard
from datetime import datetime

# Создаем роутер для обработчиков
user_router = Router()

# Обработчик команды /start
@user_router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я эхо-бот. Напиши что-нибудь, и я повторю.",
        reply_markup=create_inline_keyboard()
    )

# Обработчик команды /help
@user_router.message(F.text == "/help")
async def cmd_help(message: Message):
    await message.answer(
        "Это мой первый бот созданный с помощью Python\n"
        "Список команд:\n"
        "/start — начать работу\n"
        "/help — помощь"
    )



# Обработчик для фото
@user_router.message(F.photo)
async def echo_photo(message: Message):
    await message.answer_photo(
        message.photo[-1].file_id,
        caption=f"Вы отправили фото!"
    )


# Обработчик для видео
@user_router.message(F.video)
async def echo_video(message: Message):
    await message.answer_video(
        message.video.file_id,
        caption="Вы отправили видео!"
    )


# Обработчик для файлов
@user_router.message(F.document)
async def echo_document(message: Message):
    await message.answer_document(
        message.document.file_id,
        caption="Вы отправили файл!"
    )


@user_router.message(F.text == "/info")
async def cmd_info(message: Message):
    user = message.from_user
    reg_date = message.date.astimezone().strftime("%d.%m.%Y %H:%M")
    await message.answer(
        f"👤 ID: <code>{user.id}</code>\n"
        f"📛 Имя: {user.full_name}\n"
        f"🕒 Дата регистрации: {reg_date}",
        parse_mode="HTML"
    )


# Обработчик текстовых сообщений (эхо)
@user_router.message(F.text)
async def echo_message(message: Message):
    await message.answer(
        f"Вы написали: {message.text}",
        reply_markup=create_inline_keyboard()
    )