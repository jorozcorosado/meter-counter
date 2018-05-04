#!/usr/bin/python3

import RPi.GPIO as GPIO
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
import serial
import time

pnconfig = PNConfiguration()

pnconfig.subscribe_key = 'Your-Pubnub-Subscribe-Key-Here'
pnconfig.publish_key = 'Your-Pubnub-Publish-Key-Here'

pubnub = PubNub(pnconfig)

channel = 'Channel-Name-Here'

ser = serial.Serial('/dev/ttyACM0',9600)

while True:                                          
    a = int(ser.readline(),16)
    c = time.time()
    b = (a*7.48/1000)
    d=round(b,3)
    print(d)
    class MyListener(SubscribeCallback):
        def publish_callback(result, status):
            pass
    pubnub.publish().channel("awesomeChannel").message({'Meter': d, 'time': c}).sync()
                
    pubnub.add_listener(MyListener())
    pubnub.subscribe().channels(channel).execute()                
