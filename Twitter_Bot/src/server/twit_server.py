import picamera


camera = picamera.Picamera()

camera.capture('image.jpg')


print 'took a pic'


