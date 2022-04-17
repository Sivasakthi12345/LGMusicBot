#
# Copyright (C) 2021-2022 by LOGI-LAB@Github, < https://github.com/LOGI-LAB >.
#
# This file is part of < https://github.com/LOGI-LAB/LGMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/LOGI-LAB/LGMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from LGMusic.core.bot import LGBot
from LGMusic.core.dir import dirr
from LGMusic.core.git import git
from LGMusic.core.userbot import Userbot
from LGMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = LGBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
