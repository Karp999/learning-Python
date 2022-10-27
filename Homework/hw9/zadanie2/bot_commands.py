from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import *

async def BonjourCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Bonjour, {update.effective_user.first_name} !:)') #что пишет в терминале

async def SumCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    values = update.message.text
    print(values)
    items = values.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Сумма равна: {x}+{y}={x+y}')

async def SubCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    values = update.message.text
    print(values)
    items = values.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Разность {x} и {y} равна {x-y}')

async def DivCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    values = update.message.text
    print(values)
    items = values.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Частное {x} и {y} равно {x/y}')

async def ProdCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    values = update.message.text
    print(values)
    items = values.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'Произведение {x} и {y} равно {x*y}')


async def HelpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/sum\n/sub\n/div\n/prod\n/help\n') #примеры вызова команд

