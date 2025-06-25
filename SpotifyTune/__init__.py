from SpotifyTune.core.bot import Spotify
from SpotifyTune.core.dir import dirr
from SpotifyTune.core.git import git
from SpotifyTune.core.userbot import Userbot
from SpotifyTune.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Spotify()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
