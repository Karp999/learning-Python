from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from logger import *
import emoji 
from random import randint

candy = 2021


#команда приветствия
async def BonjourCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f"Приветствуем, {update.effective_user.first_name} !😊\nДля отображения меню чата нажмите => /help ") #что пишет в терминале
#команда описания условий игры
async def StartCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f"Вы играете в игру '2021 конфета'🍬\nПосле жеребьёвки Вы и Бот по очереди забираете не более 28 конфет.\nПобеждает тот, кто сделает крайний ход.😊\n\nДля начала жеребьёвки нажмите => /lot\nДля возврата в меню чата нажмите => /help") #что пишет в терминале
#команда начала игры - жеребьёвка
async def GameLotCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    lottery = randint(0, 1)
    if lottery == 1: 
        first = update.effective_user.first_name
        second = "Бот"
        await update.message.reply_text("🖐🏼 "+first+", первый ход ваш, а затем - "+second+"\n\nДля начала игры нажмите => /game\nДля возврата в меню чата нажмите => /help")
    else: 
        first = "Бот"
        second = update.effective_user.first_name
        await update.message.reply_text("🤖 Первым ходит "+first+", а затем - "+second+"\n\nДля начала игры нажмите => /game\nДля возврата в меню чата нажмите => /help")



async def CompMove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    while candy > 0:
        botMove = randint(0, 28)
        await update.message.reply_text("Бот берет",botMove,"конфет 🍬.") #копия снизу
        if botMove > candy:
            botMove = candy
        # await update.message.reply_text("Бот берет",candy,"конфет 🍬.")
        candy = candy - botMove
        botSumCandy = botSumCandy + botMove
        await update.message.reply_text("Бот имеет", botSumCandy, "конфет.\nВ игре осталось", candy,"конфет 🍬.")

async def UserMove(update: Update, context: ContextTypes.DEFAULT_TYPE):
    while candy > 0: #цикл игры
        await update.message.reply_text(update.effective_user.first_name+", сколько вы возьмёте конфет?🍬\nВведите число от 0 до 28: ") 
        userMove = int(update.message.text)
        while userMove <= 0 or userMove > 28:
            await update.message.reply_text("❗ "+update.effective_user.first_name+", взять можно от 0 до 28 конфет, повторите ход.\nСколько вы возьмёте конфет? ")
            userMove = int(update.message.text)
        while userMove > candy:
            await update.message.reply_text("❗ "+update.effective_user.first_name+", в стопке недостаточно конфет, повторите ход.\nВзять можно от 0 до 28 единиц.\nСколько вы возьмёте конфет? ")
            userMove = int(update.message.text)
        else:
            if 0 <= userMove <= 28:
                userSumCandy = userMove + userSumCandy
                candy = candy-userMove
                await update.message.reply_text(update.effective_user.first_name+", у вас", userSumCandy, "конфет.\nВ игре осталось", candy,"конфет 🍬.")
                  



async def AGameCommand(update: Update, context: ContextTypes.DEFAULT_TYPE, ):
    log(update, context)
    lottery = randint(0, 1)
    if lottery == 1: 
        first = update.effective_user.first_name
        second = "Бот"
        await update.message.reply_text("🖐🏼 "+first+", первый ход ваш, а затем - "+second+"\n\nДля начала игры нажмите => /game\nДля возврата в меню чата нажмите => /help")
        await update.message.reply_text("Игра началась, удачи!🤗")
        UserMove()
        if candy == 0:
            userSumCandy = userSumCandy + botSumCandy
            await update.message.reply_text(update.effective_user.first_name+", поздравляем, вы победили и все конфеты ваши!🤗 Игра окончена! 🎉")
            return
    else: 
        first = "Бот"
        second = update.effective_user.first_name
        await update.message.reply_text("🤖 Первым ходит "+first+", а затем - "+second+"\n\nДля начала игры нажмите => /game\nДля возврата в меню чата нажмите => /help")
        await update.message.reply_text("Игра началась, удачи!🤗")
        CompMove()
        if candy == 0:
            botSumCandy = botSumCandy + userSumCandy
            await update.message.reply_text("🤖 Бот победил и забирает", botSumCandy, "конфет!\nИгра окончена! 🎉")
            return

    # if lottery == 1:
    #     UserMove()
    #     if candy == 0:
    #         userSumCandy = userSumCandy + botSumCandy
    #         await update.message.reply_text(update.effective_user.first_name+", поздравляем, вы победили и все конфеты ваши!🤗 Игра окончена! 🎉")
    #         return
    # else:
    #     CompMove()
    #     if candy == 0:
    #         botSumCandy = botSumCandy + userSumCandy
    #         await update.message.reply_text("🤖 Бот победил и забирает", botSumCandy, "конфет!\nИгра окончена! 🎉")
    #         return




  

    







async def GameCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    a = randint(0, 1)

    if a == 1: #жеребьёвка. первое условие - первым ходит пользователь
        first = update.effective_user.first_name
        second = "Бот"
        await update.message.reply_text("🖐🏼 "+first+", первый ход ваш, а затем - "+second+"\n\nДля начала игры нажмите => /game\nДля возврата в меню чата нажмите => /help")
        await update.message.reply_text("Игра началась, удачи!🤗")

        # if message.text == "/Go":
        #     bot.send_message(message.chat.id, f'Введи количество конфет от 1 до 28', reply_markup=get_board(numb))
        # else:
        #     bot.send_message(message.chat.id, 'Что-то не так. Попробуем еще раз')
        #     bot.register_next_step_handler(message, get_candy)


        while candy > 0: #цикл игры
            await update.message.reply_text(update.effective_user.first_name+", сколько вы возьмёте конфет?🍬\nВведите число от 0 до 28: ") 
            userMove = int(update.message.from_user)
            while userMove <= 0 or userMove > 28:
                await update.message.reply_text("❗ "+update.effective_user.first_name+", взять можно от 0 до 28 конфет, повторите ход.\nСколько вы возьмёте конфет? ")
                userMove = int(update.message.from_user)
            while userMove > candy:
                await update.message.reply_text("❗ "+update.effective_user.first_name+", в стопке недостаточно конфет, повторите ход.\nВзять можно от 0 до 28 единиц.\nСколько вы возьмёте конфет? ")
                userMove = int(update.message.from_user)
            else:
                if 0 <= userMove <= 28:
                    userSumCandy = userMove + userSumCandy
                    candy = candy-userMove
                    await update.message.reply_text(update.effective_user.first_name+", у вас", userSumCandy, "конфет.\nВ игре осталось", candy,"конфет 🍬.")
                    if candy == 0:
                        userSumCandy = userSumCandy + botSumCandy
                        await update.message.reply_text(update.effective_user.first_name+", поздравляем, вы победили и все конфеты ваши!🤗 Игра окончена! 🎉")
                        return

            botMove = randint(0, 28)
            await update.message.reply_text("Бот берет",botMove,"конфет 🍬.") #копия снизу
            if botMove > candy:
                botMove = candy
                await update.message.reply_text("Бот берет",candy,"конфет 🍬.")
            candy = candy - botMove
            botSumCandy = botSumCandy + botMove
            await update.message.reply_text("Бот имеет", botSumCandy, "конфет.\nВ игре осталось", candy,"конфет 🍬.")

            if candy == 0:
                botSumCandy = botSumCandy + userSumCandy
                await update.message.reply_text("🤖 Бот победил и забирает", botSumCandy, "конфет!\nИгра окончена! 🎉")
                return
    else: #второе условие - первым ходит бот
        first = "Бот"
        second = update.effective_user.first_name
        await update.message.reply_text("🤖 Первым ходит "+first+", а затем - "+second)
        await update.message.reply_text("Игра началась, удачи!🤗")
        while candy > 0: 
            botMove = randint(0, 28)
            await update.message.reply_text("Бот берет",botMove,"конфет 🍬.") #копия снизу
            if botMove > candy:
                botMove = candy
                await update.message.reply_text("Бот берет", candy,"конфет 🍬.")
            candy = candy - botMove
            botSumCandy = botSumCandy + botMove
            await update.message.reply_text("Бот имеет", botSumCandy, "конфет.\nВ игре осталось", candy,"конфет 🍬.")

            if candy == 0:
                botSumCandy = botSumCandy + userSumCandy
                await update.message.reply_text("🤖 Бот победил и забирает", botSumCandy, "конфет!\nИгра окончена! 🎉")
                return

            await update.message.reply_text(update.effective_user.first_name+", сколько вы возьмёте конфет?🍬\nВведите число от 0 до 28: ") 
            userMove = int(update.message.from_user)
            while userMove <= 0 or userMove > 28:
                await update.message.reply_text("❗ "+update.effective_user.first_name+", взять можно от 0 до 28 конфет, повторите ход.\nСколько вы возьмёте конфет? ")
                userMove = int(update.message.from_user)
            while userMove > candy:
                await update.message.reply_text("❗ "+update.effective_user.first_name+", в стопке недостаточно конфет, повторите ход.\nВзять можно от 0 до 28 единиц.\nСколько вы возьмёте конфет? ")
                userMove = int(update.message.from_user)
            else:
                if 0 <= userMove <= 28:
                    userSumCandy = userMove + userSumCandy
                    candy = candy-userMove
                    await update.message.reply_text(update.effective_user.first_name+", у вас", userSumCandy, "конфет.\nВ игре осталось", candy,"конфет 🍬.")
                    if candy == 0:
                        userSumCandy = userSumCandy + botSumCandy
                        await update.message.reply_text(update.effective_user.first_name+", поздравляем, вы победили и все конфеты ваши!🤗 Игра окончена! 🎉")
                        return


#команда помощи - меню бота
async def HelpCommand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f"МЕНЮ БОТА:\n\n/hi - приветствие 😊\n/start - описание условий игры 📑\n/lot - жеребьёвка 🎲\n/game - начало игры '2021 конфета'🍬\n/help - помощь 🤝\n") #меню бота

