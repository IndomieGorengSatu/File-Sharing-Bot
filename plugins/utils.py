import os

from bot import Bot
from config import (
    ADMINS,
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    DB_URI,
    FORCE_MSG,
    FORCE_SUB_CHANNEL,
    OWNER_ID,
    PROTECT_CONTENT,
    START_MSG,
    TG_BOT_TOKEN,
)
from pyrogram import filters
from pyrogram.types import Message


@Bot.on_message(filters.command("indomie") & filters.user(ADMINS))
async def varsFunc(client: Bot, message: Message):
    Man = await message.reply_text("Tunggu Sebentar...")
    text = f"""<u><b>CONFIG VARS</b></u> @{client.username}
APP_ID = <code>{APP_ID}</code>
API_HASH = <code>{API_HASH}</code>
TG_BOT_TOKEN = <code>{TG_BOT_TOKEN}</code>
DATABASE_URL = <code>{DB_URI}</code>
OWNER_ID = <code>{OWNER_ID}</code>
ADMINS = <code>{ADMINS}</code>
    
<u><b>CUSTOM VARS</b></u>
CHANNEL_ID = <code>{CHANNEL_ID}</code>
FORCE_SUB_CHANNEL = <code>{FORCE_SUB_CHANNEL}</code>
PROTECT_CONTENT = <code>{PROTECT_CONTENT}</code>
START_MSG = <code>{START_MSG}</code>

FORCE_MSG = <code>{FORCE_MSG}</code>
    """
    await Man.edit_text(text)
