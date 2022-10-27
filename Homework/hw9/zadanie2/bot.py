# Прикрутить бота к задачам с предыдущего семинара:
# a. Создать калькулятор для работы с рациональными и комплексными числами, 
# организовать меню, добавив в неё систему логирования

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')
app = ApplicationBuilder().token("5653762938:AAEX45-Z4hWyZmDCje6C2wFkJFowBxuYz_M").build()

app.add_handler(CommandHandler("hi", BonjourCommand)) #название команды
app.add_handler(CommandHandler("sum", SumCommand)) #название команды
app.add_handler(CommandHandler("sub", SubCommand)) #название команды
app.add_handler(CommandHandler("div", DivCommand)) #название команды
app.add_handler(CommandHandler("prod", ProdCommand)) #название команды
app.add_handler(CommandHandler("help", HelpCommand)) #название команды

print("bot launched")
app.run_polling()

