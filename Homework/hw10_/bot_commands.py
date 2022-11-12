from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from logger import *
import emoji 
from random import randint
#команда приветствия
async def BonjourCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Приветствуем, {update.effective_user.first_name} !😊\nДля отображения меню чата введите команду: /help ') #что пишет в терминале
#команда описания условий игры
async def StartCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Вы играете в игру "2021 конфета"🍬\nПосле жеребьёвки Вы и Бот по очереди забираете не более 28 конфет.\nПобеждает тот, кто сделает крайний ход.😊') #что пишет в терминале
#команда начала игры + процесс
async def GameCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    a = randint(0, 1)
    if a == 1:
        first = update.effective_user.first_name
        second = "Бот"
        await update.message.reply_text("🖐🏼 "+first+", первый ход ваш, а затем - "+second)
    else:
        first = "Бот"
        second = update.effective_user.first_name
        await update.message.reply_text("🤖 Первым ходит "+first+", а затем - "+second)

    candy = 2021
    await update.message.reply_text("Игра началась, удачи!🤗")

    if second == update.effective_user.first_name:
        while candy > 0: 
            botMove = randint(0, 28)
            if botMove > candy:
                botMove = candy
            await update.message.reply_text("Бот берет"+candy+"конфет 🍬.")
            botSumCandy = botSumCandy + botMove
            candy = candy - botMove
            await update.message.reply_text("Бот имеет", botSumCandy, "конфет.\nВ игре осталось", candy,"конфет 🍬.")

            if candy == 0:
                botSumCandy = botSumCandy + userSumCandy
                await update.message.reply_text("🤖 Бот победил и забирает", botSumCandy, "конфет!\nИгра окончена! 🎉")
                return
               
            userMove = int(input(update.effective_user.first_name+", сколько вы возьмёте конфет?🍬\nВведите число от 0 до 28: "))
            while userMove <= 0 or userMove > 28:
                userMove = int(input("❗ "+update.effective_user.first_name+", взять можно от 0 до 28 конфет, повторите ход.\nСколько вы возьмёте конфет? "))
            while userMove > candy:
                userMove = int(input("❗ "+update.effective_user.first_name+", в стопке недостаточно конфет, повторите ход.\nВзять можно от 0 до 28 единиц.\nСколько вы возьмёте конфет? "))
            else:
                if 0 <= userMove <= 28:
                    userSumCandy = userMove + userSumCandy
                    candy = candy-userMove
                    print (update.effective_user.first_name+", у вас", userSumCandy, "конфет.\nВ игре осталось", candy,"конфет 🍬.")
                    if candy == 0:
                        userSumCandy = userSumCandy + botSumCandy
                        print(update.effective_user.first_name+", поздравляем, вы победили и все конфеты ваши!🤗 Игра окончена! 🎉")
                        return
    else:
        while candy > 0: 
            userMove = int(input(update.effective_user.first_name+", сколько вы возьмёте конфет?🍬\nВведите число от 0 до 28: "))
            while userMove <= 0 or userMove > 28:
                userMove = int(input("❗ "+update.effective_user.first_name+", взять можно от 0 до 28 конфет, повторите ход.\nСколько вы возьмёте конфет? "))
            while userMove > candy:
                userMove = int(input("❗ "+update.effective_user.first_name+", в стопке недостаточно конфет, повторите ход.\nВзять можно от 0 до 28 единиц.\nСколько вы возьмёте конфет? "))
            else:
                if 0 <= userMove <= 28:
                    userSumCandy = userMove + userSumCandy
                    candy = candy-userMove
                    print (update.effective_user.first_name+", у вас", userSumCandy, "конфет.\nВ игре осталось", candy,"конфет 🍬.")
                    if candy == 0:
                        userSumCandy = userSumCandy + botSumCandy
                        print(update.effective_user.first_name+", поздравляем, вы победили и все конфеты ваши!🤗 Игра окончена! 🎉")
                        return
            botMove = randint(0, 28)
            if botMove > candy:
                botMove = candy
            await update.message.reply_text("Бот берет"+candy+"конфет 🍬.")
            botSumCandy = botSumCandy + botMove
            candy = candy - botMove
            await update.message.reply_text("Бот имеет", botSumCandy, "конфет.\nВ игре осталось", candy,"конфет 🍬.")

            if candy == 0:
                botSumCandy = botSumCandy + userSumCandy
                await update.message.reply_text("🤖 Бот победил и забирает", botSumCandy, "конфет!\nИгра окончена! 🎉")
                return
    return
    
#команда помощи - меню бота
async def HelpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'МЕНЮ БОТА:\n\n/hi - приветствие 😊\n/start - описание условий игры 📑\n/game - начало игры "2021 конфета"🍬\n/help - помощь 🤝\n') #меню бота

