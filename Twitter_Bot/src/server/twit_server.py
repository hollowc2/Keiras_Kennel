import picamera
import tweepy
from credentials import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
camera = picamera.PiCamera()

camera.capture('image.jpg')


api.update_status(status="Keira loves to eat turds")

print 'took a pic'


