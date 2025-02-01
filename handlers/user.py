from aiogram import Router, F
from aiogram.types import Message
from keyboards.inline import create_inline_keyboard, create_contacts_keyboard
from aiogram.types import CallbackQuery
from keyboards.reply import create_reply_keyboard

ADMINS = [1384014428]

# Создаем роутер для обработчиков
user_router = Router()

# Обработчик команды /start
@user_router.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я эхо-бот. Напиши что-нибудь, и я повторю.",
        reply_markup=create_reply_keyboard()
    )
    await message.answer(
        "Выберете действие:",
        reply_markup=create_inline_keyboard()
    )


# Обработчик команды О боте
@user_router.message(F.text == "О боте")
async def cmd_help(message: Message):
    await message.answer(
        "Это мой первый бот созданный с помощью Python.\n"
        "Бот просто отправляет ваше сообщение обратно.\n"
        "В боте реализованы основные команды для взаимодействия с пользователем."
    )


# Обработчик команды контакты
@user_router.message(F.text == "Контакты")
async def cmd_contacts(message: Message):
    await message.answer(
        "Контакты:",
        reply_markup=create_contacts_keyboard()
    )

# Обработчк информации о пользователе
@user_router.message(F.text == "Информация о пользователе")
async def cmd_info(message: Message):
    user = message.from_user
    reg_date = message.date.astimezone().strftime("%d.%m.%Y %H:%M")
    await message.answer(
        f"👤 ID: <code>{user.id}</code>\n"
        f"📛 Имя: {user.full_name}\n"
        f"🕒 Дата регистрации: {reg_date}",
        parse_mode="HTML"
    )

# Обработчик статистики
@user_router.message(F.text == "Статистика")
async def cmd_stats(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer("Статистика бота просто космическая!!!")
    else:
        await message.answer("Этот раздел только для администрации!")



# Обработчик удаления сообщения
@user_router.callback_query(F.data == "delete")
async def delete_message(callback: CallbackQuery):
    await callback.message.delete()



# Обработчик текстовых сообщений (эхо)
@user_router.message(F.text)
async def echo_message(message: Message):
    await message.answer(
        f"Вы написали: {message.text}",
        reply_markup=create_inline_keyboard()
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
