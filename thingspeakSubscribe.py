import paho.mqtt.client as mqtt
import sys


# Callback - conexão ao broker
def conectou(client, userdata, flags, rc):
    if rc == 0:
        print('Conectado ao broker!')
    else:
        print('Não conectado, falha na conexão! Erro =', rc)
    print('Conextado ao topico', topic)
    client.subscribe(topic)


# Callback - mensagem recebida do broker
def chegou_mensagem(client, userdata, msg):
    v = msg.payload
    print(msg.topic + ' ' + v.decode())


# Programa principal
broker = 'mqtt.thingspeak.com'
topic = 'channels/1540318/subscribe/fields/field1/XNSX6X9PBYXFZ2MZ'


try:
    client = mqtt.Client()
    client.on_connect = conectou
    client.on_message = chegou_mensagem
    # client.username_pw_set('userqualquer, 'mqttapikey)
    client.connect(broker, 1883)
    client.loop_forever()
except KeyboardInterrupt:
    print("\nCtrl+C pressionado, encerrando aplicacao e saindo...")
    client.disconnect()
    sys.exit(0)
