from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

# ссылка на бота https://t.me/A_candyGame2021_bot
app = ApplicationBuilder().token("5637820658:AAEF_Tgf2qzzWgAKJwfynRgiCxcOnaPDN34").build()

app.add_handler(CommandHandler("hi", BonjourCommand)) #команда приветствия
app.add_handler(CommandHandler("start", StartCommand)) #команда описания условий игры
app.add_handler(CommandHandler("game", GameCommand)) #команда начала игры + процесс
app.add_handler(CommandHandler("help", HelpCommand)) #команда помощи - меню бота
print("bot launched") #добавила,чтоб проверять, запустился ли код
app.run_polling()

#у меня на команде game возникают ошибки. Если первый-пользователь, ошибка:
# ValueError: invalid literal for int() with base 10: '/game', то есть бот берет предыдущее значение, а не введенное число для продолжения кода
# если первый бот, ошибка: telegram.error.BadRequest: Unsupported parse_mode
# я еще не нашла выхода из этих ошибок, поэтому сама игра у меня на ступоре.
# есть идея переписать все библиотекой telebot, о этот вариант проще, поэтому добиваю библиотеку telegram
#register_next_step_handler(message, func) - в документации telegram не нашла подобной команды из telebot
# @bot.callback_query_handler(func) - тоже не нашла, в поиске