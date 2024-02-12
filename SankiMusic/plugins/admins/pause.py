from pyrogram import filters
from pyrogram.types import Message

from SankiMusic.utilities.config import BANNED_USERS
from SankiMusic.utilities.strings import get_command
from SankiMusic import bot
from SankiMusic.modules.core.call import Kaal
from SankiMusic.modules.main.database import is_music_playing, music_off
from SankiMusic.modules.main.decorators import AdminRightsCheck
from SankiMusic.utilities.events.filters import command
from SankiMusic.utilities.inline.play import close_keyboard

# Commands
PAUSE_COMMAND = get_command("PAUSE_COMMAND")


@bot.on_message(
    command(PAUSE_COMMAND)
    & filters.group
    & ~BANNED_USERS
)
@AdminRightsCheck
async def pause_admin(cli, message: Message, _, chat_id):
    if not len(message.command) == 1:
        return await message.reply_text(_["general_2"])
    if not await is_music_playing(chat_id):
        return await message.reply_text(_["admin_1"])
    await music_off(chat_id)
    await Kaal.pause_stream(chat_id)
    await message.reply_text(
        _["admin_2"].format(message.from_user.first_name),
        reply_markup=close_keyboard
    )
