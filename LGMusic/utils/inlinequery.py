#
# Copyright (C) 2021-2022 by LOGI-LAB@Github, < https://github.com/LOGI-LAB >.
#
# This file is part of < https://github.com/LOGI-LAB/LGMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/LOGI-LAB/LGMusicBot/blob/master/LICENSE >
#
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="𝐏𝐚𝐮𝐬𝐞 𝐒𝐭𝐫𝐞𝐚𝐦",
            description=f"ᴘᴀᴜꜱᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://te.legra.ph/file/0d882277912ab980e65b2.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="𝐑𝐞𝐬𝐮𝐦𝐞 𝐒𝐭𝐫𝐞𝐚𝐦",
            description=f"ʀᴇꜱᴜᴍᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/02d1b7f967ca11404455a.png",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="𝐌𝐮𝐭𝐞 𝐒𝐭𝐫𝐞𝐚𝐦",
            description=f"ᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="𝐔𝐧𝐦𝐮𝐭𝐞 𝐒𝐭𝐫𝐞𝐚𝐦",
            description=f"ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
        InlineQueryResultArticle(
            title="𝐒𝐤𝐢𝐩 𝐒𝐭𝐫𝐞𝐚𝐦",
            description=f"ꜱᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | ꜰᴏʀ ꜱᴘᴇᴄɪꜰɪᴄ ᴛʀᴀᴄᴋ ɴᴜᴍʙᴇʀ: /ꜱᴋɪᴘ [ɴᴜᴍʙᴇʀ] ",
            thumb_url="https://telegra.ph/file/98b88e52bc625903c7a2f.png",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="𝐄𝐧𝐝 𝐒𝐭𝐫𝐞𝐚𝐦",
            description="ꜱᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/d2eb03211baaba8838cc4.png",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="𝐂𝐫𝐞𝐚𝐭𝐨𝐫",
            description="ᴀʙᴏᴜᴛ ʟɢ ʙᴏᴛꜱ ꜱᴏᴄɪᴇᴛʏ ᴏᴡɴᴇʀ.",
            thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
            input_message_content=InputTextMessageContent("@aboutlogesh"),
        ),
        InlineQueryResultArticle(
            title="𝐒𝐡𝐮𝐟𝐟𝐥𝐞 𝐒𝐭𝐫𝐞𝐚𝐦",
            description="ꜱʜᴜꜰꜰʟᴇ ᴛʜᴇ Qᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋꜱ ʟɪꜱᴛ.",
            thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="𝐒𝐞𝐞𝐤 𝐒𝐭𝐫𝐞𝐚𝐦",
            description="ꜱᴇᴇᴋ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ꜱᴛʀᴇᴀᴍ ᴛᴏ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ᴅᴜʀᴀᴛɪᴏɴ.",
            thumb_url="https://telegra.ph/file/cd25ec6f046aa8003cfee.png",
            input_message_content=InputTextMessageContent("/seek 10"),
        ),
        InlineQueryResultArticle(
            title="𝐋𝐨𝐨𝐩 𝐒𝐭𝐫𝐞𝐚𝐦",
            description="ʟᴏᴏᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜꜱɪᴄ. | ᴜꜱᴀɢᴇ: /ʟᴏᴏᴘ [ᴇɴᴀʙʟᴇ|ᴅɪꜱᴀʙʟᴇ]",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)
