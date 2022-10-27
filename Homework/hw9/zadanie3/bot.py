# Прикрутить бота к задачам с предыдущего семинара:
# b. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token("5799576275:AAENLVLN4Be-HJfdNVqRjqQyOtFNbCEGQLc").build()

app.add_handler(CommandHandler("phonebook", hello))
print("bot launched")
app.run_polling()