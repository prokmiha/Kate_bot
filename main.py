import logging
import asyncio
import os
from datetime import date

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import NetworkError

from kinoterapy import Kinoterapy
from regeneration import Regeneration
from bot_handler import BotHandler

# git push heroku master
bot_token = os.environ.get('BOT_TOKEN')

bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

bot_handler = BotHandler(dp)
regeneration = Regeneration(dp, bot)
kinoterapy = Kinoterapy(dp, bot)
next_session_date = date(2024, 9, 9)
current_date = date.today()


async def start_bot():
	while True:
		try:
			await dp.start_polling(reset_webhook=True)
		except NetworkError:
			logging.error('Network error occurred. Restarting bot...')
			await asyncio.sleep(5)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	await bot_handler.start_command(message)


@dp.message_handler(text='До початку')
async def return_to_start(message: types.Message):
	await start_command(message)


@dp.callback_query_handler(lambda query: query.data == 'main_menu')
async def main_menu_inline(callback_query: types.CallbackQuery):
	message = callback_query.message
	await start_command(message)


@dp.message_handler(lambda message: message.text == 'Збірка віршів «Регенерація»')
async def regeneration_start(message: types.Message):
	await regeneration.startup_menu(message)


@dp.message_handler(lambda message: message.text == 'Інструкція')
async def regeneration_instruction(message: types.Message):
	await regeneration.process_instruction(message)


@dp.message_handler(lambda message: message.text == 'Придбати')
async def regeneration_purchase(message: types.Message):
	await regeneration.process_purchase(message)


@dp.callback_query_handler(lambda query: query.data == 'copy_email')
async def regeneration_email(query: types.CallbackQuery):
	await regeneration.copy_email_handler(query)


@dp.message_handler(lambda message: message.text == 'Кінотерапія')
async def kinoterapy_start(message: types.Message):
	if current_date < next_session_date:
		await kinoterapy.kinoterapy_not_allowed(message)
	else:
		await kinoterapy.kinoterapy_startup_menu(message)


@dp.message_handler(lambda message: message.text == 'Сплатити')
async def kinoterapy_purchase(message: types.Message):
	await kinoterapy.kinoterapy_process_purchase(message)


@dp.message_handler(lambda message: message.text == 'Програма кінотерапії')
async def kinoterapy_purchase(message: types.Message):
	await kinoterapy.kinoterapy_process_taryph(message)


@dp.callback_query_handler(lambda query: query.data == 'copy_email')
async def kinoterapy_email(query: types.CallbackQuery):
	await kinoterapy.kinoterapy_copy_email_handler(query)


@dp.message_handler()
async def echo(message: types.Message):
	await bot_handler.echo(message)


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	try:
		loop.create_task(start_bot())
		loop.run_forever()
	finally:
		loop.run_until_complete(storage.close())
		loop.run_until_complete(storage.wait_closed())
		loop.close()
