#!/usr/bin/python3
import RPi.GPIO as GPIO
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'Your-Pubnub-Subscribe-Key-Here'
pnconfig.publish_key = 'Your-Pubnub-Publish-Key-Here'

pubnub = PubNub(pnconfig)

channel = 'Channel-Name-Here'

def setup_gpio():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)


def on(gpio):
    print("Turning ON GPIO {gpio}".format(gpio=gpio))    
    GPIO.output(int(gpio), GPIO.HIGH)

def off(gpio):
    print("Turning OFF GPIO {gpio}".format(gpio=gpio))
    GPIO.output(int(gpio), GPIO.LOW)

class Listener(SubscribeCallback):
    def message(self, pubnub, message):
        msg = message.message
        if 'action' in msg and msg['action'] == 'on':
            on(msg['gpio'])
        if 'action' in msg and msg['action'] == 'off':
            off(msg['gpio'])
            
setup_gpio()
print('Listening...')
pubnub.add_listener(Listener())
pubnub.subscribe().channels(channel).execute()
