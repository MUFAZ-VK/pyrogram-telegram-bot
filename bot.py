from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


API_ID = 000000  
API_HASH = "your_api_hash"
BOT_TOKEN = "your_bot_token"

app = Client(
    "pyrogram-telegram-bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@app.on_message(filters.command("start"))
async def start(client, message):
    keyboard = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("💡 About", callback_data="about")],
            [InlineKeyboardButton("📢 Channel", url="https://t.me/bot_resurge")],
            [InlineKeyboardButton("👨‍💻 Developer", url="https://t.me/realmufaz")]
        ]
    )
    await message.reply_text(
        text=f"👋 Hey {message.from_user.mention}!\n\nWelcome to **My Pyrogram Bot** 🚀",
        reply_markup=keyboard
    )

@app.on_callback_query()
async def callback_query(client, callback_query):
    if callback_query.data == "about":
        await callback_query.message.edit_text(
            "This is a **Pyrogram bot** with inline buttons.\n\nMade with ❤️ by @realmufaz"
        )

app.run()
