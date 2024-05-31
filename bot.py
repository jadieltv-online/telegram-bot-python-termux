from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Função para lidar com o comando /start
def start(update, context):
    update.message.reply_text('Olá! Eu sou um bot do Telegram.')

# Função para lidar com mensagens de texto
def echo(update, context):
    update.message.reply_text(update.message.text)

def main():
    # Inicializar o updater com o token do seu bot
    updater = Updater("7473664216:AAF4VmVs1-5oQWnHx-T-ckdVeN0t8JaTWro", use_context=True)

    # Obter o despachante para registrar manipuladores
    dp = updater.dispatcher

    # Registrar um manipulador para o comando /start
    dp.add_handler(CommandHandler("start", start))

    # Registrar um manipulador para mensagens de texto
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Iniciar o bot
    updater.start_polling()

    # Manter o bot em execução até Ctrl+C ser pressionado
    updater.idle()

if __name__ == '__main__':
    main()
