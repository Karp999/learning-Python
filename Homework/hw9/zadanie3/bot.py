# Прикрутить бота к задачам с предыдущего семинара:
# b. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# МОЙ БОТ - @A_phonebook_bot

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = ApplicationBuilder().token("5799576275:AAENLVLN4Be-HJfdNVqRjqQyOtFNbCEGQLc").build()

app.add_handler(CommandHandler("phonebook", hello))
app.add_handler(CommandHandler("phonebook", hello))
app.add_handler(CommandHandler("phonebook", hello))
app.add_handler(CommandHandler("phonebook", hello))
app.add_handler(CommandHandler("phonebook", hello))


print("bot launched")
app.run_polling()