from aiogram import types
import os


class Kinoterapy:
	def __init__(self, dp, bot):
		self.dp = dp
		self.bot = bot

	@staticmethod
	async def kinoterapy_startup_menu(message: types.Message):
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(types.KeyboardButton(text='Програма кінотерапії'))
		keyboard.add(types.KeyboardButton(text='Оплатити'))
		keyboard.add(types.KeyboardButton(text='До початку'))

		await message.answer(
			"""Привіт-привіт 💫 
Кінотерапія вже зачекалася на тебе 🥰

<code>Тебе чекає подорож, тривалістю 15 днів, де ти віднайдеш однодумців, нові погляди на творчість, нові скіли по відео, натхнення і, найголовніше, — себе! </code>""",
			reply_markup=keyboard, parse_mode='HTML')

	@staticmethod
	async def kinoterapy_process_taryph(message: types.Message):
		await message.answer(
			"""Програма кінотерапії: 

<b>Перший ефір</b> — знайомство + теорія по відео;
Окремо, на каналі, будуть додаткові матеріали у відео і текстовому форматі; 

<b>Другий ефір</b> — розбір помилок, відповіді на запитання + додаткові матеріали по відео;

<b>Третій ефір</b> — Моя історія життя. Як біль конвертується у кохання і як це впливає на творчість. Відкриваємо душі і прощаємося із обмеженнями;

<b>Четвертий ефір</b> — Дівочі теревеньки; 

<b>Пʼятий (останній ефір)</b> — підбиття підсумків.""",
			parse_mode='HTML')
		await message.answer(
			"На кожному із ефірів я дам тобі завдання на виконання, яке необхідно відтворити до наступного ефіру")

	@staticmethod
	async def kinoterapy_process_purchase(message: types.Message):
		keyboard_hide = types.ReplyKeyboardRemove()  # Удаляем клавиатуру

		await message.answer(
			"""<i>Кожен мною написаний твір несе в собі важливі послання.
		Сподіваюсь, що з ними ти віднайдеш клаптик віри, жменю надії і двісті пʼятдесят грамів тепла, що приведуть тебе до спокою і любові❤️</i>""",
			reply_markup=keyboard_hide, parse_mode="HTML")
		await message.answer(f'''Оплатити своє місце у кінотерапії можливо двома способами: 

 • Карта монобанк 
<code>{os.environ.get('CARD_1')}
Катерина Война</code> 

Сума в гривнях: 
1650 грн — пакет без зворотнього зв’язку 
2930 грн — пакет зі зворотнім зв’язком від мене 

Щоб сплатити на європейський рахунок: 
<code>{os.environ.get('CARD_2')}
Kateryna Voina</code> 

Сума в евро: 
41€ — пакет без зворотнього зв’язку 
73€ — зі зворотнім зв’язком від мене особисто ''', parse_mode="HTML")

		keyboard = types.InlineKeyboardMarkup()
		email_button = types.InlineKeyboardButton(text='Електронна адреса', callback_data='copy_email')
		chat_button = types.InlineKeyboardButton(text='Написати в особисті', url='https://t.me/kate_voina')
		main_menu_button = types.InlineKeyboardButton(text='До початку', callback_data='main_menu')
		keyboard.add(email_button, chat_button, main_menu_button)

		message_text = """Після оплати, надішли будь-ласка скрін оплати в особисті повідомлення 🫶🏼\
там ти отримаєш усі посилання з доступом до спільного чату і головоного каналу ✨"""
		await message.answer(message_text, reply_markup=keyboard)

	async def kinoterapy_copy_email_handler(self, query: types.CallbackQuery):
		email = 'regenerationpoetry@gmail.com'

		if query.from_user.is_bot:
			pass
		else:
			await self.bot.send_message(chat_id=query.from_user.id, text=f"Адреса електронної пошти: {email}")
