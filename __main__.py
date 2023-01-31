@@ -0,0 +1,157 @@

@@ -1,30 +1,30 @@

import sys

import qithon

from qithon import BOTLOG_CHATID, HEROKU_APP, PM_LOGGER_GROUP_ID

from .Config import Config

from .core.logger import logging

from .core.session import qiiq

from .utils import (

    add_bot_to_logger_group,

    install_externalrepo,

    ipchange,

    load_plugins,

    setup_bot,

    mybot,

    startupmessage,

    verifyLoggerGroup,

    saves,

)

LOGS = logging.getLogger("qithon")

print(qithon.copyright)

print("Licensed under the terms of the " + qithon.license)

cmdhr = Config.COMMAND_HAND_LER

try:

    LOGS.info("جارِ بدء بوت ميوس ✓")

    LOGS.info("جارِ بدء بوت بابل ✓")

    qiiq.loop.run_until_complete(setup_bot())

    LOGS.info("تم اكتمال تنصيب البوت ✓")

except Exception as e:

    LOGS.error(f"{str(e)}")

    sys.exit()

try:

    LOGS.info("يتم تفعيل وضع الانلاين")

    jepiq.loop.run_until_complete(mybot())

    LOGS.info("تم تفعيل وضع الانلاين بنجاح ✓")

except Exception as qi:

    LOGS.error(f"- {qi}")

    sys.exit()    

class CatCheck:

    def init(self):

        self.sucess = True

Catcheck = CatCheck()

async def startup_process():

    check = await ipchange()

    if check is not None:

        Catcheck.sucess = False

        return

    await verifyLoggerGroup()

    await load_plugins("plugins")

    await load_plugins("assistant")

    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    print("︙بـوت ميوس بابل يعـمل بـنجاح ")

    print(

        f"تم تشغيل الانلاين تلقائياً ارسل {cmdhr}الاوامر لـرؤيـة اوامر السورس\

        \nللمسـاعدة تواصـل  https://t.me/spportm"

    )

    print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

    await verifyLoggerGroup()

    await saves()

    await add_bot_to_logger_group(BOTLOG_CHATID)

    if PM_LOGGER_GROUP_ID != -100:

        await add_bot_to_logger_group(PM_LOGGER_GROUP_ID)

    await startupmessage()

    Catcheck.sucess = True

    return

async def externalrepo():

    if Config.VCMODE:

        await install_externalrepo("https://github.com/qithoniq/JepVc", "jepvc", "jepthonvc")

qiiq.loop.run_until_complete(externalrepo())

qiiq.loop.run_until_complete(startup_process())

if len(sys.argv) not in (1, 3, 4):

    qiiq.disconnect()

elif not Catcheck.sucess:

    if HEROKU_APP is not None:

        HEROKU_APP.restart()

else:

    try:

        qiiq.run_until_disconnected()

    except ConnectionError:

        pass
