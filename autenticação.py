import tweepy
import autenticacao as aut

auth = tweepy.OAuthHandler(aut.API_key, aut.API_key_secret)
auth.set_access_token(aut.access_token, aut.access_token_secret)

api = tweepy.API(auth)

# Envia o tweet
tweet = 'Teste IoT!'
try:
    api.update_status(tweet)
    print(tweet)
except tweepy.TweepError as e:
    print(e.reason)
