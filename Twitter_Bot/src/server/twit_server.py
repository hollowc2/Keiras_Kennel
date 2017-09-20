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





def tweet_image(url, message):
    api = twitter_api()
    filename = 'image.jpg'
    request = requests.get(url, stream=True)
    if requests.status_code == 200:
        with open(filename, 'wb') as image:
            for chunk in request:
                image.write(chunk)

        api.update_with_media(filename, status=message)
        os.remove(filename)
    else:
        print("Unalbe to download image")

url = 'image.jpg'
message = "Cheese"
tweet_image(url)



print 'took a pic'


