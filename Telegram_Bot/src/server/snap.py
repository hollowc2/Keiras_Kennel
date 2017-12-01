import picamera
import os
from time import sleep
from fractions import Fraction


#Todo
#1. Add timestamp to image name
#2.
#

image = 'image.jpg'
camera = picamera.PiCamera()
camera.vflip = True
camera.brightness = 58
camera.exposure_mode='auto'

print 'camera initilized'

def snapIt():
    camera.capture(image)
    return image
