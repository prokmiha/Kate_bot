from aiogram import types, Dispatcher, Bot

from kate_bot.database import db
from kate_bot.filters.group_filter import IsGroupAdmin


async def setup_handlers(dp: Dispatcher, bot: Bot):
    @dp.message_handler(IsGroupAdmin())
    async def ban_unauthorized_user(message: types.Message):
        pass
        #
        # user_id = message.from_user.id
        #
        #
        #     await bot.ban_chat_member(chat_id=message.chat.id, user_id=user_id)
        #     await types.ChatActions.typing(2)
        #     await bot.unban_chat_member(chat_id=message.chat.id, user_id=user_id)

        # all_users = await bot.get_chat_members_count(chat_id=-1001992782164)
        # print(all_users)