from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("5637820658:AAEF_Tgf2qzzWgAKJwfynRgiCxcOnaPDN34").build()


app.add_handler(CommandHandler("hi", BonjourCommand)) #команда приветствия
app.add_handler(CommandHandler("start", StartCommand)) #команда начала игры
app.add_handler(CommandHandler("lottery", LotteryCommand)) #команда жеребьёвки
app.add_handler(CommandHandler("sub", SubCommand)) #название команды
app.add_handler(CommandHandler("div", DivCommand)) #название команды
app.add_handler(CommandHandler("prod", ProdCommand)) #название команды
app.add_handler(CommandHandler("help", HelpCommand)) #название команды
print("bot launched") #сами добавили,чтоб проверить, запустился ли код
app.run_polling()
