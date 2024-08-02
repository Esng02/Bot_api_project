from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
import os
import requests

API_TOKEN = os.getenv("TELEGRAM_API_TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Отправляет приветственное сообщение при запуске бота.
    """
    await message.reply("Привет! Нажми /messages для получения сообщения и /create для создания своего")


@dp.message(commands=['messages'])
async def fetch_messages(message: types.Message):
    """
    Получает список сообщений от FastAPI и отправляет их пользователю.
    """
    response = requests.get("http://web:8000/api/v1/messages/")
    messages = response.json()
    if messages:
        formatted_messages = "\n".join([f"{msg['author']}: {msg['content']}" for msg in messages])
    else:
        formatted_messages = "Ничего не найддено."
    await message.reply(formatted_messages)


@dp.message(commands=['create'])
async def create_message(message: types.Message):
    """
    Просит пользователя отправить сообщение для создания.
    """
    await message.reply("Отправь свое сообщения")


@dp.message()
async def echo(message: types.Message):
    """
    Отправляет текст сообщения на FastAPI для сохранения.
    """
    response = requests.post("http://web:8000/api/v1/message/", json={
        "author": message.from_user.username,
        "content": message.text
    })
    if response.status_code == 200:
        await message.reply("Сообщение создано!")
    else:
        await message.reply("Произошла какая то ошибка :(. \nСообщение не создано.")

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
