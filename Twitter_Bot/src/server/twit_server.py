import picamera
import tweepy
import requests
import os
from credentials import *

def twitter_api():

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return api

camera = picamera.PiCamera()
camera.capture('image.jpg')
api = twitter_api()
api.update_with_media('image.jpg', status="Heres my face")
print 'took a pic'


