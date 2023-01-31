             await jepiq(JoinChannelRequest(channel=lMl10l))

        except OverflowError:

            LOGS.error("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")

            continue

async def load_plugins(folder, extfolder=None):

    """

    تحميل ملفات السورس

    """

    if extfolder:

        path = f"{extfolder}/*.py"

        plugin_path = extfolder

    else:

        path = f"qithon/{folder}/*.py"

        plugin_path = f"qithon/{folder}"

    files = glob.glob(path)

    files.sort()

    success = 0

    failure = []

    for name in files:

        with open(name) as f:

            path1 = Path(f.name)

            shortname = path1.stem

            pluginname = shortname.replace(".py", "")

            try:

                if (pluginname not in Config.NO_LOAD) and (

                    pluginname not in VPS_NOLOAD

                ):

                    flag = True

                    check = 0

                    while flag:

                        try:

                            load_module(

                                pluginname,

                                plugin_path=plugin_path,

                            )

                            if shortname in failure:

                                failure.remove(shortname)

                            success += 1

                            break

                        except ModuleNotFoundError as e:

                            install_pip(e.name)

                            check += 1

                            if shortname not in failure:

                                failure.append(shortname)

                            if check > 5:

                                break

                else:

                    os.remove(Path(f"{plugin_path}/{shortname}.py"))

            except Exception as e:

                if shortname not in failure:

                    failure.append(shortname)

                os.remove(Path(f"{plugin_path}/{shortname}.py"))

                LOGS.info(

                    f"لم يتم تحميل {shortname} بسبب خطأ {e}\nمسار الملف {plugin_path}"

                )

    if extfolder:

        if not failure:

            failure.append("None")

        await qiiq.tgbot.send_message(

            BOTLOG_CHATID,

            f'- تم بنجاح استدعاء الاوامر الاضافيه \n**عدد الملفات التي استدعيت:** `{success}`\n**فشل في استدعاء :** `{", ".join(failure)}`',

        )

async def verifyLoggerGroup():

    """

    Will verify the both loggers group

    """

    flag = False

    if BOTLOG:

        try:

            entity = await jepiq.get_entity(BOTLOG_CHATID)

            if not isinstance(entity, types.User) and not entity.creator:

                if entity.default_banned_rights.send_messages:

                    LOGS.info(

                        "🤦︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."

                    )

                if entity.default_banned_rights.invite_users:

                    LOGS.info(

                        "🌚︙الفار الأذونات مفقودة لإرسال رسائل لـ PRIVATE_GROUP_BOT_API_ID المحدد."

                    )

        except ValueError:

            LOGS.error("🌚︙تـأكد من فـار المجـموعة  PRIVATE_GROUP_BOT_API_ID.")

        except TypeError:

            LOGS.error(

                "🌚︙لا يمكـن العثور على فار المجموعه PRIVATE_GROUP_BOT_API_ID. تأكد من صحتها."

            )

        except Exception as e:

            LOGS.error(

                "🌚︙حدث استثناء عند محاولة التحقق من PRIVATE_GROUP_BOT_API_ID.\n"

                + str(e)

            )

    else:

        descript = "- عزيزي المستخدم هذه هي مجموعه الاشعارات يرجى عدم حذفها  - @Jepthon"

        photobt = await qiiq.upload_file(file="JepIQ/razan/resources/start/Jepthon.JPEG")

        _, groupid = await create_supergroup(

            "مجموعة أشعارات الجوكر ", jepiq, Config.TG_BOT_USERNAME, descript, photobt

        )

        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)

        print("🌚︙تم إنشاء مجموعة المسـاعدة بنجاح وإضافتها إلى المتغيرات.")

        flag = True

    if PM_LOGGER_GROUP_ID != -100:

        try:

            entity = await qiiq.get_entity(PM_LOGGER_GROUP_ID)

            if not isinstance(entity, types.User) and not entity.creator:

                if entity.default_banned_rights.send_messages:

                    LOGS.info(

                        "🌚︙الأذونات مفقودة لإرسال رسائل لـ PM_LOGGER_GROUP_ID المحدد."

                    )

                if entity.default_banned_rights.invite_users:

                    LOGS.info(

                        "🌚︙الأذونات مفقودة للمستخدمين الإضافيين لـ PM_LOGGER_GROUP_ID المحدد."

                    )

        except ValueError:

            LOGS.error("🌚︙لا يمكن العثور على فار  PM_LOGGER_GROUP_ID. تأكد من صحتها.")

        except TypeError:

            LOGS.error("🌚︙PM_LOGGER_GROUP_ID غير مدعوم. تأكد من صحتها.")

        except Exception as e:

            LOGS.error(

                "⌯︙حدث استثناء عند محاولة التحقق من PM_LOGGER_GROUP_ID.\n" + str(e)

            )

    else:

        descript = "🌚︙ وظيفه الكروب يحفظ رسائل الخاص اذا ما تريد الامر احذف الكروب نهائي \n  - @Jepthon"

        photobt = await qiiq.upload_file(file="qiIQ/razan/resources/start/Jepthon2.JPEG")

        _, groupid = await create_supergroup(

            "مجموعة التخزين", jepiq, Config.TG_BOT_USERNAME, descript, photobt

        )

        addgvar("PM_LOGGER_GROUP_ID", groupid)

        print("تـم عمـل الكروب التخزين بنـجاح واضافة الـفارات الـيه.")

        flag = True

    if flag:

        executable = sys.executable.replace(" ", "\\ ")

        args = [executable, "-m", "qithon"]

        os.execle(executable, *args, os.environ)

        sys.exit(0)

async def install_externalrepo(repo, branch, cfolder):

    QITHONREPO = repo

    rpath = os.path.join(cfolder, "requirements.txt")

    if JEPTHONBRANCH := branch:

        repourl = os.path.join(QITHONREPO, f"tree/{QITHONBRANCH}")

        gcmd = f"git clone -b {QITHONBRANCH} {QITHONREPO} {cfolder}"

        errtext = f"لا يوحد فرع بأسم `{QITHONBRANCH}` في الريبو الخارجي {QITHONREPO}. تاكد من اسم الفرع عبر فار (`EXTERNAL_REPO_BRANCH`)"

    else:

        repourl = JEPTHONREPO

        gcmd = f"git clone {QITHONREPO} {cfolder}"

        errtext = f"الرابط ({QITHONREPO}) الذي وضعته لفار `EXTERNAL_REPO` غير صحيح عليك وضع رابط صحيح"

    response = urllib.request.urlopen(repourl)

    if response.code != 200:

        LOGS.error(errtext)

        return await jepiq.tgbot.send_message(BOTLOG_CHATID, errtext)

    await runcmd(gcmd)

    if not os.path.exists(cfolder):

        LOGS.error(

            "هنالك خطأ اثناء استدعاء رابط الملفات الاضافية يجب التأكد من الرابط اولا "

        )

        return await qiiq.tgbot.send_message(

            BOTLOG_CHATID,

            "هنالك خطأ اثناء استدعاء رابط الملفات الاضافية يجب التأكد من الرابط اولا ",

        )

    if os.path.exists(rpath):

        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")

    await load_plugins(folder="qithon", extfolder=cfolder)


#!/bin/bash


_get_ziplink () {
    local regex
    regex='(https?)://github.com/.+/.+'
    if [[ $UPSTREAM_REPO == "jepthoniq" ]]
    then
        echo "aHR0cHM6Ly9naXRodWIuY29tL2plcHRob25pcS9qZXB0aG9uL2FyY2hpdmUvSGVyb2t1LnppcA==" | base64 -d
    elif [[ $UPSTREAM_REPO =~ $regex ]]
    then
        if [[ $UPSTREAM_REPO_BRANCH ]]
        then
            echo "${UPSTREAM_REPO}/archive/${UPSTREAM_REPO_BRANCH}.zip"
        else
            echo "${UPSTREAM_REPO}/archive/Heroku.zip"
        fi
    else
        echo "aHR0cHM6Ly9naXRodWIuY29tL2plcHRob25pcS9qZXB0aG9uL2FyY2hpdmUvSGVyb2t1LnppcA==" | base64 -d
    fi
}

_get_repolink () {
    local regex
    local rlink
    regex='(https?)://github.com/.+/.+'
    if [[ $UPSTREAM_REPO == "jepthoniq" ]]
    then
        rlink=`echo "aHR0cHM6Ly9naXRodWIuY29tL2plcHRob25pcS9qZXB0aG9uLmdpdA==" | base64 -d`
    elif [[ $UPSTREAM_REPO =~ $regex ]]
    then
        rlink=`echo "${UPSTREAM_REPO}"`
    else
        rlink=`echo "aHR0cHM6Ly9naXRodWIuY29tL2plcHRob25pcS9qZXB0aG9uLmdpdA==" | base64 -d`
    fi
    echo "$rlink"
}


_run_python_code() {
    python3${pVer%.*} -c "$1"
}

_run_catpack_git() {
    $(_run_python_code 'from git import Repo
import sys
OFFICIAL_UPSTREAM_REPO = "https://github.com/jepthoniq/jepthon"
ACTIVE_BRANCH_NAME = "Heroku"
repo = Repo.init()
origin = repo.create_remote("temponame", OFFICIAL_UPSTREAM_REPO)
origin.fetch()
repo.create_head(ACTIVE_BRANCH_NAME, origin.refs[ACTIVE_BRANCH_NAME])
repo.heads[ACTIVE_BRANCH_NAME].checkout(True) ')
}

_run_cat_git() {
    local repolink=$(_get_repolink)
    $(_run_python_code 'from git import Repo
import sys
OFFICIAL_UPSTREAM_REPO="'$repolink'"
ACTIVE_BRANCH_NAME = "'$UPSTREAM_REPO_BRANCH'" or "Heroku"
repo = Repo.init()
origin = repo.create_remote("temponame", OFFICIAL_UPSTREAM_REPO)
origin.fetch()
repo.create_head(ACTIVE_BRANCH_NAME, origin.refs[ACTIVE_BRANCH_NAME])
repo.heads[ACTIVE_BRANCH_NAME].checkout(True) ')
}

_set_bot () {
    local zippath
    zippath="joker.zip"
    echo "جاري تنزيل اكواد السورس "
    wget -q $(_get_ziplink) -O "$zippath"
    echo " تفريغ البيانات "
    CATPATH=$(zipinfo -1 "$zippath" | grep -v "/.");
    unzip -qq "$zippath"
    echo " تم التفريغ "
    echo " يتم التنظيف "
    rm -rf "$zippath"
    sleep 5
    _run_catpack_git
    cd $CATPATH
    _run_cat_git
    python3 ../setup/updater.py ../requirements.txt requirements.txt
    chmod -R 755 bin
    echo "   بدء تنزيل بيانات بابل ميوس   "
    echo "
    "
    python3 -m joker
}

_set_bot
