from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5637820658:AAEF_Tgf2qzzWgAKJwfynRgiCxcOnaPDN34").build()


app.add_handler(CommandHandler("hi", BonjourCommand)) #команда приветствия
app.add_handler(CommandHandler("start", StartCommand)) #команда описания условий игры
app.add_handler(CommandHandler("game", GameCommand)) #команда начала игры + процесс
app.add_handler(CommandHandler("help", HelpCommand)) #команда помощи - меню бота
print("bot launched") #добавила,чтоб проверять, запустился ли код
app.run_polling()

