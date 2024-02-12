from aiohttp import ClientSession
from .console import LOGGER

from SankiMusic.modules.core.app import Qwertz
from SankiMusic.modules.core.bot import Bot
from SankiMusic.modules.core.dirs import dirr
from SankiMusic.modules.core.git import git
from SankiMusic.misc import dbb, heroku, sudo

dirr()
git()
dbb()
heroku()

# Clients
app = Bot()

bot = Qwertz()


from SankiMusic.utilities.media import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
