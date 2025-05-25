import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# قراءة التوكن و ID الأدمن من متغيرات البيئة
BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

if BOT_TOKEN is None or ADMIN_ID is None:
    raise ValueError("يجب ضبط متغيرات البيئة: BOT_TOKEN و ADMIN_ID")

# تحويل ADMIN_ID إلى int
ADMIN_ID = int(ADMIN_ID)

# دالة الرد على أي رسالة
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"استلمت رسالتك: {user_message}")

# إعداد البوت
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # التعامل مع أي رسالة نصية
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("البوت شغال الآن...")
    app.run_polling()

if __name__ == "__main__":
    main()
