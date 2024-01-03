from aiogram.types import Message, ChatMemberStatus
from aiogram.dispatcher.filters import BoundFilter


class IsGroupAdmin(BoundFilter):
    async def check(self, message: Message):
        chat_id = message.chat.id
        channel_info = await message.bot.get_chat(chat_id)

        # Вывод информации о канале
        print(f"ID канала: {chat_id}")
        print(f"Название канала: {channel_info.title}")

        # Обработка сообщения из канала
        print(f"Получено сообщение из канала {channel_info.title}: {message.text}")
