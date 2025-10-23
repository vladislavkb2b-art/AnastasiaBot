import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from config import BOT_TOKEN, ADMIN_ID
from handlers import client_menu, admin_panel, booking

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Регистрация роутеров
dp.include_router(client_menu.router)
dp.include_router(admin_panel.router)
dp.include_router(booking.router)

@dp.message(Command('start'))
async def start(message: types.Message):
    text = (

        '💎 <b>Добро пожаловать к Anastasia Usmanova!</b>\n\n'

        'Выберите действие 👇'

    )
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    keyboard.add('💆 Услуги и прайс')

    keyboard.add('🎁 Акции')

    keyboard.add('📅 Записаться')

    keyboard.add('💬 Задать вопрос')

    await message.answer(text, reply_markup=keyboard)


async def main():

    print('🤖 Бот запущен')

    await dp.start_polling(bot)


if __name__ == '__main__':

    asyncio.run(main())

