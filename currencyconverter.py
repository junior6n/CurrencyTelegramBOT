import logging
from telegram import Update
from telegram.ext import Updater, ContextTypes, CommandHandler, ApplicationBuilder
import conversion_devis
import os

logging.basicConfig(
    format='%(astime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO    
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Hello {update.effective_user.first_name}, This is a currency converter bot\n type the command /help for available commands ")

async def convert(update: Update, context: ContextTypes.DEFAULT_TYPE):
    montant = context.args[0]
    code = context.args[1]
    code2 = context.args[3]
    n_montant = conversion_devis.convert(code, code2, montant)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"{montant}{code} = {n_montant}{code2}")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, text="""
This is a currency converter bot, available commande
/help : Pour afficher de l'aide
/convert : Pour convertir le devis d'un montant e.g /convert 500 XAF in USD 
"""
    )

async def converter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pass    

if __name__ == '__main__':
    token = os.environ.get('TELEGRAM_BOT_TOKEN')
    application = ApplicationBuilder().token(f'{token}').build()

    start_handler = CommandHandler('start', start)
    convert_handler = CommandHandler('convert', convert)
    help_handler = CommandHandler('help', help)

    application.add_handler(convert_handler)
    application.add_handler(start_handler)
    application.add_handler(help_handler)

    application.run_polling()