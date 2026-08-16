import os
import threading
import telebot
from flask import Flask
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaVideo

# ================= 🌐 FLASK SERVER (Render Keep-Alive) =================
app = Flask(__name__)

@app.route('/')
def home():
    return 'Bot is Alive!'

def run_flask():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

threading.Thread(target=run_flask, daemon=True).start()

# ================= ⚙️ CONFIGURATION =================

BOT_TOKEN = os.environ.get("BOT_TOKEN", "8686847961:AAGdiPHVtcWuD69t312TuLVCiW2nJcWPfEU")

OWNER_ID = 6509210563
ADMIN_LIST = [OWNER_ID, 8770711577]

UPI_ID = "Lodhi.219@superyes"
PAYMENT_NAME = "Pallavi Lodhi"

VIP_ZIP_LINK = "https://t.me/goodbfyh"
VIP_HUB_LINK = "https://t.me/+sFJS3ZsRu29hNDU1"

# ================= 🎥 VIDEO FILE IDs =================

START_VIDEOS = [
    "BAACAgUAAxkBAAMPanj7WJ03eLJC9SpuTRPsJBsC5HAAAlonAALe5chXh1r_idW46GU9BA",
    "BAACAgUAAxkBAAMOanj7WFhYiWHyafjELabpDyNJeocAAlknAALe5chXUQTDMAc70s09BA",
    "BAACAgUAAxkBAAMQanj7WApn6sXxzlzM4CvqcSfp2OoAAlsnAALe5chXDuCVUshUVRo9BA",
    "BAACAgUAAxkBAAMSanj7WD7fmbUNzz1tLo7OvAWxnrcAAl0nAALe5chX8PoYuRpfo3o9BA",
    "BAACAgUAAxkBAAMRanj7WFm35dJyPKPnFoCKHa2NVGkAAlwnAALe5chXwNieSnqb7Gk9BA"
]

PLAN_1_VIDEOS = [
    "BAACAgUAAxkBAAM4ankH11g4i5z0miNgKrG17m6VXQMAAl4nAALe5chXvPMahhQjpC09BA",
    "BAACAgUAAxkBAAM5ankH1xyroYyIIUPL89TyA4ypwGkAAl8nAALe5chX0wnJd3MGXoM9BA",
    "BAACAgUAAxkBAAM6ankH13058b1JwVSESZB62rxNepwAAmAnAALe5chXSeFunBTo3Hs9BA",
    "BAACAgUAAxkBAAM7ankH15rtmQOV0U231KFOTESYoMYAAmEnAALe5chXpdOIRDJawoQ9BA",
    "BAACAgUAAxkBAAM8ankH116B71eKo3vPq4wC8eNIyeYAAmInAALe5chX2Z0IM8JgVWw9BA"
]

PLAN_2_VIDEOS = [
    "BAACAgUAAxkBAANOankJd5PfCxgIzMHSwBZmZjFAqzQAAmQnAALe5chXh7fr3AzlMEM9BA",
    "BAACAgUAAxkBAANPankJdxCFI5IBfjJXMdngAxqlG-8AAmYnAALe5chXbKXLFrpm_wk9BA",
    "BAACAgUAAxkBAANNankJd_28TrhgLBp8HAdCDwVN0U0AAmMnAALe5chXu22A8JSuHmc9BA",
    "BAACAgUAAxkBAANQankJdysvJb5cGHaqrYz8hpiNARUAAmcnAALe5chXEok6RJKa_io9BA",
    "BAACAgUAAxkBAANRankJd00sVtRdqmsLTRK6d30zFksAAmgnAALe5chX3gABasBM92iQPQQ"
]

PLAN_3_VIDEOS = [
    "BAACAgUAAxkBAANaankKbeaYSI2NbJJpvotkETACvfYAAmonAALe5chXK9IZ25WJ91w9BA",
    "BAACAgUAAxkBAANZankKbaBAVK8NsYHDxTlEh5r_tUgAAmknAALe5chX3zIe2CLgLuc9BA",
    "BAACAgUAAxkBAANQankJdysvJb5cGHaqrYz8hpiNARUAAmcnAALe5chXEok6RJKa_io9BA",
    "BAACAgUAAxkBAANRankJd00sVtRdqmsLTRK6d30zFksAAmgnAALe5chX3gABasBM92iQPQQ",
    "BAACAgUAAxkBAANNankJd_28TrhgLBp8HAdCDwVN0U0AAmMnAALe5chXu22A8JSuHmc9BA"
]

PLAN_4_VIDEOS = [
    "BAACAgUAAxkBAANoankMwv8aGNdlY4WbiJgCh5Cr2O8AAmwnAALe5chXl9oyFHOAmjE9BA",
    "BAACAgUAAxkBAANnankMwpCQshs9v_FUQASuCRxlS5cAAmsnAALe5chXYdR8Rq2zfE89BA",
    "BAACAgUAAxkBAANqankMwmsrq-3HUbqBNLLzMTLAEN4AAm4nAALe5chXGXEabpFvrrc9BA",
    "BAACAgUAAxkBAANpankMwpHMeENXOF_y29qJcLnelE4AAm0nAALe5chXbWvvl3MhYms9BA",
    "BAACAgUAAxkBAANrankMwg_cOQABXnvLuS359gF-6E0ZAAJvJwAC3uXIVyJWso4q3H1mPQQ"
]

PLAN_5_VIDEOS = [
    "BAACAgUAAxkBAAN3ankN_p6RZxRwx8gKAd5W3mGiMgsAAnEnAALe5chXmzpWXJkY7TE9BA",
    "BAACAgUAAxkBAAN2ankN_gHxCbsppCuFcsY4lS-joxEAAnAnAALe5chX_jdzNq7ymLw9BA",
    "BAACAgUAAxkBAAN4ankN_tnPgXAV-x65rhcWc5kOtFYAAnInAALe5chX8anxsb07u-E9BA",
    "BAACAgUAAxkBAAN5ankN_kq_uh1Mw6K94CBqftZBt5cAAnMnAALe5chX123Yi5djiig9BA",
    "BAACAgUAAxkBAAN6ankN_vAvoQ4YOjQ4RYcD0r--3GgAAnQnAALe5chXa_HUF3UV8kM9BA"
]

HOW_TO_USE_VIDEO = "BAACAgUAAxkBAAOhankd0IeeaIEw_WMWszMi0MOzxCUAAsEfAALU08lX32fRlFGHe3w9BA"

bot = telebot.TeleBot(BOT_TOKEN)

# ================= 🎬 VIDEO SENDER (ALBUM FORMAT) =================
def send_video_list(chat_id, video_list):
    valid_ids = [vid for vid in video_list if not vid.startswith("ID_")]
    if not valid_ids:
        return

    media_group = [InputMediaVideo(media=vid_id) for vid_id in valid_ids]
    
    try:
        if len(media_group) == 1:
            bot.send_video(chat_id, valid_ids[0])
        elif len(media_group) > 1:
            bot.send_media_group(chat_id, media_group)
    except Exception:
        for vid_id in valid_ids:
            try:
                bot.send_video(chat_id, vid_id)
            except Exception:
                pass

# ================= 📱 MAIN MENU =================
def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("⚡ ALL VIDEO ⚡ -- ₹149 1M VIDEO", callback_data="pay_plan1"))
    markup.add(InlineKeyboardButton("🌽 CHILD CHORN 🌽-- ₹98 20K+ VIDEO", callback_data="pay_plan2"))
    markup.add(InlineKeyboardButton("💋 MOM SON,S 💋 📷-- ₹98 20K+ VIDEO", callback_data="pay_plan3"))
    markup.add(InlineKeyboardButton("📁 ✨ VIRAL MMS-LEAK ✨ -- ₹98  20K+ VIDEO", callback_data="pay_plan4"))
    markup.add(InlineKeyboardButton("👄 INDIAN RAPE 📷  -- ₹98 20K+ VIDEO", callback_data="pay_plan5")) 
    markup.row(
        InlineKeyboardButton("How to use ❓", callback_data="how_to_use"),
        InlineKeyboardButton("Report Issue 📩", callback_data="report_issue")
    )
    return markup

# ================= 🚀 /START COMMAND (PRIVATE CHAT ONLY) =================
@bot.message_handler(commands=['start'])
def start_cmd(message):
    if message.chat.type != 'private':
        return

    try:
        send_video_list(message.chat.id, START_VIDEOS)
        welcome_text = "👋 Hello! Welcome to **VIP MEDIA**!\n\n👇 Choose a plan to get lifetime VIP access:"
        bot.send_message(message.chat.id, welcome_text, reply_markup=main_menu(), parse_mode="Markdown")
    except Exception as e:
        print(f"Start command error: {e}")

@bot.callback_query_handler(func=lambda call: call.data == "main_menu")
def back_to_menu(call):
    if call.message.chat.type != 'private':
        return
    bot.send_message(call.message.chat.id, "👋 Welcome back! Choose a plan:", reply_markup=main_menu())

# ================= 💳 CATEGORY & PAYMENT HANDLER =================
@bot.callback_query_handler(func=lambda call: call.data.startswith("pay_plan"))
def handle_category_click(call):
    if call.message.chat.type != 'private':
        return

    plan_code = call.data
    amount = "98"
    plan_name = "VIP Pass"

    if plan_code == "pay_plan1":
        send_video_list(call.message.chat.id, PLAN_1_VIDEOS)
        amount = "149"
        plan_name = "All In One VIP Pass"
    elif plan_code == "pay_plan2":
        send_video_list(call.message.chat.id, PLAN_2_VIDEOS)
        plan_name = "Exclusive Pack"
    elif plan_code == "pay_plan3":
        send_video_list(call.message.chat.id, PLAN_3_VIDEOS)
        plan_name = "Special Collection"
    elif plan_code == "pay_plan4":
        send_video_list(call.message.chat.id, PLAN_4_VIDEOS)
        plan_name = "Mega Zip Pack"
    elif plan_code == "pay_plan5":
        send_video_list(call.message.chat.id, PLAN_5_VIDEOS)
        plan_name = "Multi-Link VIP Hub"

    pay_text = (
        f"💳 **UPI ID:** `{UPI_ID}`\n"
        f"📱 Please scan the QR and pay, then click 'I have paid' ✅\n"
        f"💰 Amount: ₹{amount}\n"
        f"♾️ Lifetime Access | 🎬 10+ Min Full Video\n"
        f"⚡ Instant Delivery After Payment\n"
        f"🚫 No Extra Charges\n"
        f"💯 No Fake / Dead Links"
    )

    pay_markup = InlineKeyboardMarkup()
    pay_markup.add(InlineKeyboardButton("I have paid ✅", callback_data="i_have_paid"))
    pay_markup.add(InlineKeyboardButton("Cancel ❌", callback_data="main_menu"))

    qr_url = f"https://api.qrserver.com/v1/create-qr-code/?size=300x300&data=upi://pay?pa={UPI_ID}&pn={PAYMENT_NAME}&am={amount}&cu=INR"

    try:
        bot.send_photo(call.message.chat.id, qr_url, caption=pay_text, reply_markup=pay_markup, parse_mode="Markdown")
    except Exception:
        bot.send_message(call.message.chat.id, pay_text, reply_markup=pay_markup, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "i_have_paid")
def i_have_paid(call):
    if call.message.chat.type != 'private':
        return
    bot.send_message(call.message.chat.id, "📸 **Please send your payment screenshot.**", parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data in ["how_to_use", "report_issue"])
def extra_info(call):
    if call.message.chat.type != 'private':
        return

    if call.data == "how_to_use":
        try:
            bot.send_video(call.message.chat.id, HOW_TO_USE_VIDEO, caption="📖 **How to Use / Payment Process:**\n1. Select any plan.\n2. Pay via UPI & send screenshot here.")
        except Exception:
            bot.send_message(call.message.chat.id, "📖 How to use:\n1. Select any plan.\n2. Pay via UPI & send screenshot here.")
    elif call.data == "report_issue":
        bot.send_message(call.message.chat.id, "📩 Report Issue:\nAgar koi dikkat hai toh message ya screenshot bhej dein.")

# ================= 📩 SCREENSHOT FORWARDING =================
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if message.chat.type != 'private':
        return

    bot.reply_to(message, "⏳ **Checking your payment.... Please wait 5-10 min.**", parse_mode="Markdown")

    for admin_id in ADMIN_LIST:
        try:
            markup = InlineKeyboardMarkup()
            markup.row(
                InlineKeyboardButton("✅ Grant VIP Access", callback_data=f"approve_{message.from_user.id}"),
                InlineKeyboardButton("❌ Fake / Reject", callback_data=f"reject_{message.from_user.id}")
            )
            bot.send_photo(
                admin_id, 
                message.photo[-1].file_id, 
                caption=f"📩 **New Payment Screenshot!**\nUser ID: `{message.from_user.id}`\n\n*(Right-swipe to reply to user)*",
                reply_markup=markup,
                parse_mode="Markdown"
            )
        except Exception:
            pass

# ================= 💬 USER TEXT MESSAGES =================
@bot.message_handler(func=lambda message: message.chat.id not in ADMIN_LIST and not message.text.startswith('/'))
def handle_user_text(message):
    if message.chat.type != 'private':
        return

    bot.reply_to(message, "⏳ **Message received! Support team will reply shortly.**", parse_mode="Markdown")
    
    for admin_id in ADMIN_LIST:
        try:
            bot.send_message(
                admin_id,
                f"💬 **New Message from User!**\nUser ID: `{message.from_user.id}`\n\nMessage: {message.text}\n\n*(Right-swipe to reply)*",
                parse_mode="Markdown"
            )
        except Exception:
            pass

# ================= 💬 ADMIN REPLIED TO USER =================
@bot.message_handler(func=lambda message: message.chat.id in ADMIN_LIST and message.reply_to_message is not None)
def handle_admin_reply(message):
    replied_msg = message.reply_to_message
    target_user_id = None

    text_source = replied_msg.caption if replied_msg.caption else replied_msg.text

    if text_source and "User ID:" in text_source:
        try:
            target_user_id = int(text_source.split("User ID:")[1].split()[0].replace("`", ""))
        except Exception:
            target_user_id = None

    if target_user_id:
        try:
            bot.send_message(target_user_id, f"💬 **Support Reply:**\n\n{message.text}", parse_mode="Markdown")
            bot.reply_to(message, "✅ **Message sent!**", parse_mode="Markdown")
        except telebot.apihelper.ApiTelegramException as e:
            if e.error_code == 403:
                bot.reply_to(message, "❌ **Error:** User ne bot ko block kar diya hai ya kabhi DM mein start nahi kiya.")
            else:
                bot.reply_to(message, f"❌ Error: {str(e)}")
        except Exception as e:
            bot.reply_to(message, f"❌ User ko message nahi gaya: {str(e)}")
    else:
        bot.reply_to(message, "⚠️ User ID nahi mil saki. Sahi message par reply karein.")

# ================= 🔓 VIP ACCESS APPROVAL & REJECTION =================
@bot.callback_query_handler(func=lambda call: call.data.startswith(("approve_", "reject_")))
def handle_admin_action(call):
    action, user_id = call.data.split("_")
    user_id = int(user_id)

    if action == "approve":
        vip_markup = InlineKeyboardMarkup()
        vip_markup.add(InlineKeyboardButton("📁 ZIP File Channel", url=VIP_ZIP_LINK))
        vip_markup.add(InlineKeyboardButton("🔗 Multi-Link VIP Hub", url=VIP_HUB_LINK))

        try:
            bot.send_message(
                user_id,
                "🎉 **PAYMENT VERIFIED! VIP ACCESS UNLOCKED!** 🎉\n\nVIP Channels join karne ke liye niche click karein:",
                reply_markup=vip_markup
            )
            bot.answer_callback_query(call.id, "✅ VIP Access Granted!")
            bot.edit_message_caption(
                chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                caption=call.message.caption + "\n\n🟢 **STATUS: APPROVED ✅**",
                parse_mode="Markdown"
            )
        except Exception as e:
            bot.answer_callback_query(call.id, f"❌ Error: {str(e)}")

    elif action == "reject":
        try:
            bot.send_message(
                user_id,
                "❌ **PAYMENT NOT RECEIVED!**\n\nAapka screenshot/payment verify nahi ho paya hai. Kripya sahi payment screenshot bhejrein.",
                parse_mode="Markdown"
            )
            bot.answer_callback_query(call.id, "❌ Fake Payment Alert Sent!")
            bot.edit_message_caption(
                chat_id=call.message.chat.id, 
                message_id=call.message.message_id, 
                caption=call.message.caption + "\n\n🔴 **STATUS: REJECTED (FAKE) ❌**",
                parse_mode="Markdown"
            )
        except Exception as e:
            bot.answer_callback_query(call.id, f"❌ Error: {str(e)}")

# File ID Finder
@bot.message_handler(content_types=['video'])
def get_video_id(message):
    if message.chat.type == 'private':
        bot.reply_to(message, f"📹 Video File ID:\n`{message.video.file_id}`", parse_mode="Markdown")

print("🤖 Bot Started Successfully!")
bot.infinity_polling()
