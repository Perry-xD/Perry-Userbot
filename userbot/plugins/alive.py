import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from userbot.sql.gvar_sql import gvarstat
from . import *

#-------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>๐ฅ๐ฅษฆษสสษฎึt ษจs ึีผสษจีผษ๐ฅ๐ฅ</b></i>

<i><b>โผ รwรฑรชr โ</i></b> : ใ <a href='tg://user?id={}'>{}</a> ใ
โญโโโโโโโโโโโโโโ
โฃโ <b>ยป Telethon ~</b> <i>{}</i>
โฃโ <b>ยป Hรชllแบรธโ  ~</b> <i>{}</i>
โฃโ <b>ยป Sudo ~</b> <i>{}</i>
โฃโ <b>ยป Uptime ~</b> <i>{}</i>
โฃโ <b>ยป Ping ~</b> <i>{}</i>
โฐโโโโโโโโโโโโโโ
<b><i>ยปยปยป <a href='https://t.me/its_userbot'>[ โ hรช Hรชllแบรธโ  ]</a> ยซยซยซ</i></b>
"""
#-------------------------------------------------------------------------------

@bot.on(hell_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(event):
    start = datetime.datetime.now()
    hell = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    a = gvarstat("ALIVE_PIC")
    if a is not None:
        b = a.split(" ")
        c = ["https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"]
        if len(b) >= 1:
            for d in b:
                c.append(d)
        PIC = random.choice(c)
    else:
        PIC = "https://telegra.ph/file/ea9e11f7c9db21c1b8d5e.mp4"
    hell_pic = PIC
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(ForGo10God, HELL_USER, tel_ver, hell_ver, is_sudo, uptime, ling)
    await event.client.send_file(event.chat_id, file=hell_pic, caption=omk, parse_mode="HTML")
    await hell.delete()


msg = """{}\n
<b><i>๐ ๐ฑ๐๐ ๐๐๐๐๐๐ ๐</b></i>
<b>Telethon โ</b>  <i>{}</i>
<b>Hรชllแบรธโ  โ</b>  <i>{}</i>
<b>Uptime โ</b>  <i>{}</i>
<b>Abuse โ</b>  <i>{}</i>
<b>Sudo โ</b>  <i>{}</i>
"""
botname = Config.BOT_USERNAME

@bot.on(hell_cmd(pattern="hell$"))
@bot.on(sudo_cmd(pattern="hell$", allow_sudo=True))
async def hell_a(event):
    uptime = await get_time((time.time() - StartTime))
    am = gvarstat("ALIVE_MSG") or "<b>ยปยป ะฝัโโะฒฯั ฮนั ฯะธโฮนะธั ยซยซ</b>"
    try:
        hell = await event.client.inline_query(botname, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg.format(am, tel_ver, hell_ver, uptime, abuse_m, is_sudo), parse_mode="HTML")


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "hell", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "โ Harmless Module"
).add()
