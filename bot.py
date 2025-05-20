import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# تحميل متغيرات البيئة من ملف .env
load_dotenv()

# قراءة التوكن ومعرف الأدمن من متغيرات البيئة
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))  # تأكد أنه عدد صحيح

# دالة الرد على الرسائل
async def reply_to_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    user_id = update.effective_user.id

    if user_id == ADMIN_ID:
        await update.message.reply_text(f"أهلًا أدمن! قلت: {user_message}")
    else:
        await update.message.reply_text("هذا البوت مخصص للإدارة فقط.")

# دالة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أرسل أي رسالة، وسأرد عليك إذا كنت الأدمن.")

# تشغيل البوت
if __name__ == '__main__':
    if not TOKEN:
        raise ValueError("يرجى ضبط BOT_TOKEN في متغيرات البيئة أو ملف .env")

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_to_message))

    print("البوت يعمل...")
    app.run_polling()
