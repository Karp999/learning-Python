from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from logger import *
import emoji
# import lottery 
from random import randint

async def BonjourCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Приветствуем, {update.effective_user.first_name} !😊\nДля отображения меню чата введите команду: /help ') #что пишет в терминале

async def StartCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Вы играете в игру "2021 конфета"🍬\nПосле жеребьёвки Вы и Бот по очереди забираете не более 28 конфет.\nПобеждает тот, кто сделает крайний ход.\nИгра началась, удачи!🤗') #что пишет в терминале


async def LotteryCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    # l = lottery.Lottery()
    a = randint(0, 1)
    if a == 1:
        await update.message.reply_text("Первый ход ваш!")
    else:
        await update.message.reply_text("Первым ходит Бот, ваш ход следующий.")


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
    await update.message.reply_text(f'МЕНЮ БОТА:\n\n/hi - приветствие 😊\n/start - начало игры "2021 конфета"🍬 \n/lottery - жеребьёвка 🎲\n/div - для нахождения частного введите вместе с операцией два числа через пробел\n/prod - для нахождения произведения введите вместе с операцией два числа через пробел\n/help - помощь 🤝\n') #меню бота

