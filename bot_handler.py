import asyncio
from datetime import datetime

from aiogram import types


class BotHandler:

	def __init__(self, dp, user_data, unic_users, none_counter):
		self.dp = dp
		# self.user_data = user_data
		# self.unic_users = unic_users
		# self.none_counter = none_counter

	async def start_command(self, message: types.Message):

		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
		keyboard.add(types.KeyboardButton(text='Збірка віршів «Регенерація»'))
		keyboard.add(types.KeyboardButton(text='Кінотерапія'))

		# user_id = message.from_user.id
		# first_name = message.from_user.first_name
		# last_name = message.from_user.last_name
		# username = message.from_user.username

		# global none_counter
		# if not username:
		# 	username = "None_" + str(self.none_counter)
		# 	self.none_counter += 1
		# if username not in self.user_data:
		# 	self.user_data[username] = {
		# 		'user_id': user_id,
		# 		'first_name': first_name,
		# 		'last_name': last_name,
		# 		'username': username
		# 	}
		#
		# print(user_id, first_name, last_name, username)

		await message.answer(
			"""Дякую за цікавість до мене, як до особистості, і до того, що я створюю. 
Усі мої продукти втілені на базі неймовірної любові до життя і до людей. 

<i>Головний мій слоган по життю — «зробити хоча б одну людину щасливішою, тоді все недарма»</i>.""",
			reply_markup=keyboard, parse_mode='HTML')
		await message.answer(
			"""<b>Наразі, я представляю два своїх продукти: 

Збірка віршів «регенерація»</b>, яка, певним чином, описує мою душу і сцілює душі інших людей;

<b>Марафон по відео «Кінотерапія»</b>, де, шляхом дослідження відео сфери, можна віднайти себе і почати відчувати цей світ по особливому, так, як живе і відчуває саме твоя душа.""",
			reply_markup=keyboard, parse_mode="HTML")

	# async def write_names_to_file(self):
	# 	while True:
	# 		await asyncio.sleep(1800)
	#
	# 		now = datetime.now()
	# 		formatted_time = now.strftime('%Y-%m-%d %H:%M:%S')
	# 		file_name = 'user_names.txt'
	#
	# 		with open(file_name, 'a', encoding="UTF-8") as file:
	#
	# 			for username, user_info in self.user_data.items():
	# 				user_id = user_info['user_id']
	# 				first_name = user_info['first_name']
	# 				last_name = user_info['last_name']
	# 				username = user_info['username']
	#
	# 				if username not in self.unic_users:
	# 					self.unic_users.append(username)
	# 					print(self.unic_users)
	# 					file.write(
	# 						f'{formatted_time}: ID: {user_id}, Name: {first_name}, Surname: {last_name}, Username: {username}\n'
	# 					)

	# @staticmethod
	async def echo(self, message: types.Message):
		if message.from_user.is_bot:
			return
		else:
			await message.delete()
