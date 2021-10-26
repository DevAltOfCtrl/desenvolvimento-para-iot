import urllib.request
import threading
import tweepy
import autenticacao as aut
import random


auth = tweepy.OAuthHandler(aut.API_key, aut.API_key_secret)
auth.set_access_token(aut.access_token, aut.access_token_secret)
api = tweepy.API(auth)


def idSensor():
    ids = [1, 2, 3]
    id_monitorado = random.choice(ids)
    return id_monitorado


def thingspeak_post():
    threading.Timer(10, thingspeak_post).start()
    id_sensor = idSensor()
    tweet_string = 'Alarme da região {} acionado'.format(id_sensor)
    URl = 'https://api.thingspeak.com/update?api_key='
    KEY = 'QIFF3RFAYVKZXT16'
    HEADER = '&field1={}'.format(id_sensor)
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data = urllib.request.urlopen(NEW_URL)
    print(data)
    try:
        api.update_status(tweet_string)
    except tweepy.TweepError as e:
        print(e.reason)


if __name__ == '__main__':
    thingspeak_post()
