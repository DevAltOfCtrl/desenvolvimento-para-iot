import time
import random
import telepot


def opcoes(msg):
    print('Chegou mensagem')
    usuario_id = msg['chat']['id']
    comando = msg['text']

    if comando == '/start':
        temperatura = random.randint(1, 100)
        if temperatura > 15:
            bot.sendMessage(usuario_id, 'O alarme disparou')
        else:
            bot.sendMessage(usuario_id, 'Temperatura dentro do normal')
    else:
        bot.sendMessage(usuario_id, 'Sistema ativo!!!')


bot = telepot.Bot('2124090203:AAEZl2FfAPhhgLhD5CUXk-ode-mH4CT6UlY')
bot.message_loop(opcoes)
print('Esperando...')

while True:
    time.sleep(1)
