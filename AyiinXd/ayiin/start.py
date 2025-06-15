from telethon import Button
from AyiinXd import (
    DEFAULT,
    DEVS,
    LOGS,
    LOOP,
    STRING_SESSION,
    blacklistayiin,
    bot,
    tgbot,
    BOTLOG_CHATID,
    BOTLOG,
)

async def startupmessage():
    """
    Start up message in telegram logger group
    """
    try:
        if BOTLOG:
            await tgbot.send_file(
                BOTLOG_CHATID,
                "https://graph.org/file/bdb46f35663ee99bde2cc-b5bc37c79774d6d76f.jpg",
                caption="𝗥𝗲𝗽𝘂𝗻𝗴𝗲𝗿-𝗨𝘀𝗲𝗿𝗯𝗼𝘁.\n     **status : Active\n     ketik `.ping` untuk cek bot!**",
                buttons=[(Button.url("Store", "https://t.me/rekberrimut")),
                         (Button.url("Proof", "https://t.me/proofimuts"))]
            )
    except Exception as e:
        LOGS.error(e)
        return None
