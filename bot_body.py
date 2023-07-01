import logging
import asyncio
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor
from aiogram.utils.exceptions import NetworkError
from constant import BOT_TOKEN, CARD_1, CARD_2

# Ініціалізація бота та зберігання станів
bot_token = BOT_TOKEN
bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

user_data = {}
unic_users = []
none_counter = 1


async def start_bot():
	while True:
		try:
			await dp.start_polling(reset_webhook=True)
		except NetworkError:
			logging.error('Network error occurred. Restarting bot...')
			await asyncio.sleep(5)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
	keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
	keyboard.add(types.KeyboardButton(text='Інструкція'))
	keyboard.add(types.KeyboardButton(text='Придбати'))

	user_id = message.from_user.id
	first_name = message.from_user.first_name
	last_name = message.from_user.last_name
	username = message.from_user.username

	global none_counter
	if not username:
		username = "None_" + str(none_counter)
		none_counter += 1
	if username not in user_data:
		user_data[username] = {
			'user_id': user_id,
			'first_name': first_name,
			'last_name': last_name,
			'username': username
		}

	print(user_id, first_name, last_name, username)

	await message.answer(
		"Привіт 🫶🏼\n\nДякую за твою цікавість до моєї першої збірки віршів <i><b>«регенерація»</b></i>.",
		reply_markup=keyboard, parse_mode='HTML')
	await message.answer("Перед тим, як придбати її, ознайомся, будь-ласка, з інструкцією", reply_markup=keyboard)


@dp.message_handler(lambda message: message.text == 'Інструкція')
async def process_training(message: types.Message):
	await message.answer(
		"""Збірку  я надішлю тобі  особисто на електронну пошту або в особисті повідомлення в телеграм."
		Натиснувши на кнопку «Придбати» ти знайдеш всі необхідні рекізити.
		<b>Після оплати, будь-ласка, надішли скріншот успішної операції на пошту або мені у особисті повідомлення</b> ✨""",
		parse_mode='HTML')
	await message.answer(
		"Якщо у тебе виникнуть запитання або складнощі, також не соромся звернутись до мене у особисті повідомлення 🥰")


@dp.message_handler(lambda message: message.text == 'Придбати')
async def process_purchase(message: types.Message):
	keyboard_hide = types.ReplyKeyboardRemove()  # Удаляем клавиатуру

	await message.answer(
		"""<i>Кожен мною написаний твір несе в собі важливі послання.
	Сподіваюсь, що з ними ти віднайдеш клаптик віри, жменю надії і двісті пʼятдесят грамів тепла, що приведуть тебе до спокою і любові❤️</i>""",
		reply_markup=keyboard_hide, parse_mode="HTML")
	await message.answer(f'''Вартість збірки: 600 грн. 
Оплатити можна двома способами: 

<b>• Карта монобанк:</b>

<code>{CARD_1}
Катерина Война</code> 

<b>• Європейський рахунок:</b> 

<code>{CARD_2}
Kateryna Voina 
Сума: 15€</code>''', parse_mode="HTML")

	keyboard = types.InlineKeyboardMarkup()
	email_button = types.InlineKeyboardButton(text='Електронна адреса', callback_data='copy_email')
	chat_button = types.InlineKeyboardButton(text='Написати в особисті', url='https://t.me/kate_voina')
	keyboard.add(email_button, chat_button)

	message_text = """Після оплати, надішли будь-ласка скрін підтвердження зручним для тебе способом — в особисті повідомлення чи на електронну пошту.

І не забувай: ти — магія. 

Обіймаю ✨"""
	await message.answer(message_text, reply_markup=keyboard)


@dp.callback_query_handler(lambda query: query.data == 'copy_email')
async def copy_email_handler(query: types.CallbackQuery):
	email = 'regenerationpoetry@gmail.com'

	if query.from_user.is_bot:
		await query.answer("Клацнув бот, а це заборонено")
	else:
		await bot.send_message(chat_id=query.from_user.id, text=f"Адреса електронної пошти: {email}")


async def write_names_to_file():
	while True:
		await asyncio.sleep(1800)

		now = datetime.now()
		formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
		file_name = 'user_names.txt'

		with open(file_name, 'a', encoding="UTF-8") as file:
			# Итерация по данным каждого пользователя в словаре
			for username, user_info in user_data.items():
				user_id = user_info['user_id']
				first_name = user_info['first_name']
				last_name = user_info['last_name']
				username = user_info['username']

				if username not in unic_users:
					unic_users.append(username)
					print(unic_users)
					file.write(
						f'{formatted_time}: ID: {user_id}, Name: {first_name}, Surname: {last_name}, Username: {username}\n'
					)


@dp.message_handler()
async def echo(message: types.Message):
	if message.from_user.is_bot:
		return  # Игнорируем сообщения от других ботов
	if message.text == 'Перезапустити бота':
		command_message = types.Message(
			message_id=message.message_id,
			chat=message.chat,
			from_user=message.from_user,
			text='/start'
		)
		await start_command(command_message)
	else:
		await message.delete()  # Удаляем сообщение


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	try:
		loop.create_task(write_names_to_file())
		loop.create_task(start_bot())
		loop.run_forever()
	finally:
		loop.run_until_complete(storage.close())
		loop.run_until_complete(storage.wait_closed())
		loop.close()
