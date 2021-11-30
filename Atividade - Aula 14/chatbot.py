import time
import random
import telepot


def opcoes(msg):
    print('Chegou mensagem')
    print('Lista de usuários ativos', ids_usuarios)
    usuario_id = msg['chat']['id']
    user = bot.getChat(usuario_id)
    nome = user['first_name']
    print('Usuário do BOT: ', usuario_id)
    comando = msg['text']
    if comando == '/cadastrar':
        if usuario_id not in ids_usuarios:
            ids_usuarios.append(usuario_id)
            nomes_usuarios.append(nome)
            bot.sendMessage(usuario_id,
                            'Usuário {} cadastrado com sucesso!'.format(nome))
    elif comando == '/descadastrar':
        if usuario_id in ids_usuarios:
            ids_usuarios.remove(usuario_id)
            nomes_usuarios.remove(nome)
            bot.sendMessage(usuario_id,
                            'Usuário {} descadastrado com\
                            sucesso!'.format(nome))
        else:
            bot.sendMessage(usuario_id,
                            'Usuário {} não está cadastrado!'.format(nome))
    elif comando == '/start':
        message = "O(a) usuário(a) {} acionou o alarme!".format(nome)
        for users in ids_usuarios:
            bot.sendMessage(chat_id=users, text=message)
        # alarme = random.randint(1, 100)
    elif comando == '/users':
        if len(nomes_usuarios) > 0:
            usuarios_cadastrados = ', '.join(nomes_usuarios)
            bot.sendMessage(usuario_id,
                            'Usuários cadastrados: {}'.format(usuarios_cadastrados))
        else:
            bot.sendMessage(usuario_id, 'Nenhum usuário cadastrado')
    else:
        bot.sendMessage(usuario_id, 'Sistema ativo!!!')


ids_usuarios = []
nomes_usuarios = []
bot = telepot.Bot('2124090203:AAEZl2FfAPhhgLhD5CUXk-ode-mH4CT6UlY')
bot.message_loop(opcoes)
print('Esperando...')


while True:
    time.sleep(1)
