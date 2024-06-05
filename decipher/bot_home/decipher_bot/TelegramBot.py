from enum import Enum, auto
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN :Final = '7448033384:AAFAebODHPDaVkDqS-XgS5u9KTOmiGf5YYw'
BOT_USERNAME :Final = '@thedecipher_bot'

integration_token: str = ''

user_state = {}



# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_reply_txt = 'This is Decipher I can curate all the learning resourses for you, and set it up on notion. /help to get started and setup your integration token and page_id to let me start making notion pages for you'
    await update.message.reply_text(start_reply_txt)
    user_state[update.message.from_user.id] = 'awaiting_integration_token'

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_reply_txt = 'You have to enter your notion integration ID and notion page id to get started. Use commands /set_integration_id to save your integration id, /set_page_id to to save your page_id under which you want to create new decipher pages'
    await update.message.reply_text(help_reply_txt)

async def set_integration_token_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_txt = 'Enter your notion integration token'
    await update.message.reply_text(reply_txt)
    user_state[update.message.from_user.id] = 'awaiting_integration_token'

    print(user_state[update.message.from_user.id])

# Responses

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id
    text = update.message.text

    if user_id in user_state:
        state = user_state[user_id]
        print(state)
        if state == 'awaiting_integration_token':
            global integration_token
            integration_token = text
            await update.message.reply_text(f'Your Notion integration token has been set to: {integration_token}')
            print(f'Your Notion integration token has been set to: {integration_token}')
            user_state.pop(user_id) #Clear the state
        else:
            print(state)
            await update.message.reply_text("I don't understand your request.")
    else:
        await update.message.reply_text("Please use a command to start")
    

def main():
    app = Application.builder().token(TOKEN).build()

    print('Bot Starting..')

    # Add command handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('set_integration_token', set_integration_token_command))

    # Add message Handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))

    # Start the Bot
    print("Bot Polling...")
    app.run_polling(poll_interval=3)


if __name__ == '__main__':
    main()
