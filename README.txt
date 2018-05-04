Special Thanks to -
Ford Motor Company

Things needed:
PubNub Account
Microsoft PowerBi Account (for mobile app)
Meter with Hall effect sensor
Arduino (101 used)
RaspberryPi (Model 3 used)

Optional -
Solenoid Valve 
Relay
Female-Male wires


Check out final product at work
(In Demo, relay or solenoid valve was no used)

https://youtu.be/nuDzvLqEIss


1. First make a free account on Pubnub.com.
2. Create a new keyset since the Publish and Subscribe keys will be needed.
3. Download both python scripts to your RaspberryPi and make sure you have the according libraries.

**Insert your publish and subscribe keys on the script and the name of the channel you want to use.(You can name it anything)
**Keep in mind that one of the scripts is for the functionality of raspberrypi through PubNub
**The other script is to read the messages sent from the arudino and publish it to PubNub

4. Download the Arduino script and upload it to your Arduino.
5. Connect USB from Arduino to the RaspberryPi.
6. Connect positive cable from meter sensor to digital pin 2 on Arduino. (Pin can be switched on Arduino script)

Everything should be connected by now, you can check if the raspberry pi is publishing the data to pubnub by using 
pubnubs debug console, just make sure to check the right channel.

------------------------------------------------------------------------------------------------------------------------------

Now for the fun part - 

7. Create an Account on Microsoft PowerBi.
8. Create a workspace on PowerBi
9. Add a PubNub streaming data set
10. Add your corresponding subscribe key from pubnub.
11. Go to your dashboard and create new tile.
12. Select your streaming data and create a clustered column chart with axis time and value meter.
13. Create new tile using streaming data set, visualization type "Card" and select field "Meter"

Now for the funcitonality, to be able to turn on and off the raspberrypis GPIOs
14. Create new tile select web content, Copy code in "Button-for-PowerBi" paste it in the content area.

** Make sure to add your subscribe key **
"value = "GPIO 11 - OFF"" 
sets the name of the button

"message : {action:"off", gpio:"11"}" 
determines what the button does... 
Make an off and on button for each GPIO

** In the Python code GPIO pins 11,13,15 were assigned as outpins and controllable through the PubNub Channel **

Check out the pinout @ https://www.marcelpost.com/wiki/images/9/90/Raspberry-pi-pinout.jpg



Copyright 2018 @Jonathan Orozco Rosado
