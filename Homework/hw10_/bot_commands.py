from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from logger import *
import emoji

async def BonjourCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Приветствуем, {update.effective_user.first_name} !😊\nВы играете в игру "2021 конфета"\nПосле жеребьёвки Вы и Бот по очереди забираете не более 28 конфет.\nПобеждает тот, кто сделает крайний ход.\nИгра началась, удачи!🤗') #что пишет в терминале


async def SumCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    values = update.message.text
    print(values)
    items = values.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Сумма равна: {x} + {y} = {x+y}')

async def SubCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    values = update.message.text
    print(values)
    items = values.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Разность равна: {x} - {y} = {x-y}')

async def DivCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    values = update.message.text
    print(values)
    items = values.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Частное равно: {x} / {y} = {x/y}')

async def ProdCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    values = update.message.text
    print(values)
    items = values.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Произведение равно: {x} * {y} = {x*y}')


async def HelpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi - приветствие\n/sum - для нахождения суммы введите вместе с операцией два числа через пробел\n/sub для нахождения разности введите вместе с операцией два числа через пробел\n/div - для нахождения частного введите вместе с операцией два числа через пробел\n/prod - для нахождения произведения введите вместе с операцией два числа через пробел\n/help - помощь\n') #примеры вызова команд

