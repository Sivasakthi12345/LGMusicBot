#
# Copyright (C) 2021-2022 by LOGI-LAB@Github, < https://github.com/LOGI-LAB >.
#
# This file is part of < https://github.com/LOGI-LAB/LGMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/LOGI-LAB/LGMusicBot/blob/master/LICENSE >
#
# All rights reserved.


class AssistantErr(Exception):
    def __init__(self, errr: str):
        super().__init__(errr)
