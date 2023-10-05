from aiogram import types


class BotHandler:

	def __init__(self, dp):
		self.dp = dp

	async def start_command(self, message: types.Message):

		keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		regeneration = (types.KeyboardButton(text='Збірка віршів «Регенерація»'))
		kinoterapy = (types.KeyboardButton(text='Кінотерапія'))
		keyboard.add(regeneration, kinoterapy)

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

	async def echo(self, message: types.Message):
		if message.from_user.is_bot:
			return
		else:
			await message.delete()
