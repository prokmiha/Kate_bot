import os
from aiogram import types

class Regeneration:
	def __init__(self, dp, bot):
		self.dp = dp
		self.bot = bot

	async def startup_menu(self, message: types.Message):
		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		instruction = (types.KeyboardButton(text='Інструкція'))
		to_buy = (types.KeyboardButton(text='Придбати'))
		to_the_beginning = (types.KeyboardButton(text='До початку'))
		keyboard.add(instruction, to_buy, to_the_beginning)

		await message.answer(
			"Привіт 🫶🏼\n\nДякую за твою цікавість до моєї першої збірки віршів <i><b>«регенерація»</b></i>.",
			reply_markup=keyboard, parse_mode='HTML')
		await message.answer("Перед тим, як придбати її, ознайомся, будь-ласка, з інструкцією", reply_markup=keyboard)

	async def process_instruction(self, message: types.Message):
		await message.answer(
			"""Збірку  я надішлю тобі  особисто на електронну пошту або в особисті повідомлення в телеграм."
			Натиснувши на кнопку «Придбати» ти знайдеш всі необхідні рекізити.
			<b>Після оплати, будь-ласка, надішли скріншот успішної операції на пошту або мені у особисті повідомлення</b> ✨""",
			parse_mode='HTML')
		await message.answer(
			"Якщо у тебе виникнуть запитання або складнощі, також не соромся звернутись до мене у особисті повідомлення 🥰")

	async def process_purchase(self, message: types.Message):
		keyboard_hide = types.ReplyKeyboardRemove()  # Удаляем клавиатуру

		await message.answer(
			"""<i>Кожен мною написаний твір несе в собі важливі послання.
		Сподіваюсь, що з ними ти віднайдеш клаптик віри, жменю надії і двісті пʼятдесят грамів тепла, що приведуть тебе до спокою і любові❤️</i>""",
			reply_markup=keyboard_hide, parse_mode="HTML")
		await message.answer(f'''Вартість збірки: 600 грн. 
	Оплатити можна двома способами: 

	<b>• Карта монобанк:</b>

		<code>{os.environ.get('CARD_1')}
	Катерина Война</code> 

	<b>• Європейський рахунок:</b> 

	<code>{os.environ.get('CARD_2')}
	Kateryna Voina 
	Сума: 15€</code>''', parse_mode="HTML")

		keyboard = types.InlineKeyboardMarkup()
		email_button = types.InlineKeyboardButton(text='Пошта', callback_data='copy_email')
		chat_button = types.InlineKeyboardButton(text='В особисті', url='https://t.me/kate_voina')
		main_menu_button = types.InlineKeyboardButton(text='До початку', callback_data='main_menu')
		keyboard.add(email_button, chat_button, main_menu_button)

		message_text = """Після оплати, надішли будь-ласка скрін підтвердження зручним для тебе способом — в особисті повідомлення чи на електронну пошту.

	І не забувай: ти — магія. 

	Обіймаю ✨"""
		await message.answer(message_text, reply_markup=keyboard)

	async def copy_email_handler(self, query: types.CallbackQuery):
		email = 'regenerationpoetry@gmail.com'
		await self.bot.send_message(chat_id=query.from_user.id, text=f"Адреса електронної пошти: {email}")