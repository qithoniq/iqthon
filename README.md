     
<h1 align="center">
  <b> TeAm Babylon |TeAm Babylon </b>
<h3 align="center">
  <b> سـورس ميـوس معتمد على مكتبة ميـوس </b>
</h3
------
اسهل طريقة للتنصيب على منصة كويب
-------------------------------------
   اسهل طريقة للتنصيب عبر الضغط على الزر في الاسفل
[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?type=git&repository=github.com/thejmthon/sbb_b0&branch=koyeb&name=jmthon-userbot&run_command=python3%20-m%20sbb_b&env%5BTG_BOT_TOKEN%5D=&env%5BAPP_ID%5D=&env%5BAPI_HASH%5D=&env%5BSTRING_SESSION%5D=&env%5BDATABASE_URL%5D=&env%5BENV%5D=ANYTHING&env%5BPM_LOGGER_GROUP_ID%5D=)
------
## التنصيب على هيروكو 
* ملاحظة: هيروكو ستصبح مدفوعة في تاريخ 28/11/2022
- احصل على فارات تنصيبك اولا واستخرجهم
- احصل على الفارات يدويا عبر [الضغط هنا](#الفارات).
- اصنع حساب على منصه هيروكو [اضغط هنا](dashboard.heroku.com)
- الان اضغط على الزر بالاسفل للتنصيب
- [![Deploy](https://www.herokucdn.com/deploy/button.svg)]([https://heroku.com/deploy](https://dashboard.heroku.com/new?template=https://github.com/thejmthon/jmthon))
------
## التنصيب محليا 
- sudo apt update && sudo apt upgrade -y
- sudo apt install --no-install-recommends -y curl git libffi-dev libjpeg-dev libwebp-dev python3-lxml python3-psycopg2 libpq-dev libcurl4-openssl-dev libxml2-dev libxslt1-dev python3-pip python3-sqlalchemy openssl wget python3 python3-dev libreadline-dev libyaml-dev gcc zlib1g ffmpeg libssl-dev libgconf-2-4 libxi6 unzip libopus0 libopus-dev python3-venv libmagickwand-dev pv tree mediainfo nano nodejs
* اذا كنت تستخدم سيرفر مجاني من شرحي استخدم الامر اما غير تجاهل الامر
- wget -N https://raw.githubusercontents.com/fscarmen/warp/main/menu.sh && bash menu.sh
* صنع قاعده بيانات داخلية
- sudo apt install postgresql postgresql-contrib
- sudo su - postgres
- psql
* هنا بدل كلمة pass بأي كلمة سر ترغب بها
- ALTER USER postgres WITH PASSWORD 'pass';
* نصنع قاعده بيانات يمكنك تغيير كلمة meos الى اي اسم او تبقيه كما هو
- CREATE DATABASE jmthon;
- \q
- exit
* سيكون شكل قاعده البيانات كـالتالي و تبدل كلمة pass مع الباسوورد الذي وضعته وكلمة Babylon مع اسم القاعدة التي وضعتها
-  postgresql://postgres:pass@localhost:5432/meos
- git clone https://github.com/Devmeos/imeos.git 
- cd imeosNJ
- sudo apt install virtualenv
- sudo apt install nano
- mv exampleconfig.py config.py
- nano config.py (املئ فارات التنصيب) -> ctrl+x -> y -> enter
- sudo apt install screen
- screen -S jmthon
- virtualenv venv
- source venv/bin/activate
- pip3 install -r requirements.txt
- python3 -m sbb_b
* نقوم بالضغط على CTRL+A بعدها نضغط على CTRL+D
------
## الفارات
- APP_ID  =  احصل عليه من هنا https://my.telegram.org
- API_HASH  =  احصل عليه من هنا https://my.telegram.org
STRING_SESSION  =  كود سيشن بابل [اضغط هنا](https://replit.com/@ssdcv608/PyroSessionString)
- TG_BOT_TOKEN  =  اصنع بوت من بوت فاذر [اضغط هنا](https://t.me/botfather) وانسخ التوكن الخاص به
- DB_URI  =  هنا قاعده البيانات 
- PRIVATE_GROUP_BOT_API_ID  =   ايدي مجموعة الحفظ
------
## تحذير هام
- غير مسؤول عن اي عملية حظر بسبب استخدامك الى هذا السورس 
- بابل تم صنعه للتسلية وجعل حسابك بشكل افضل وحماية مجمعتك
- انها مسؤليتك اذا تعرض حسابك للحذف لذلك اقتضى التنويه
 
--------------------------
# TeAm Babylon