import paho.mqtt.client as mqtt
import time
import datetime
import json

username = "YOUR USERNAME"
pasword = "YOUR PASSWORD"

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/xiaoguo/control")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def on_publish(mosq, obj, mid):
    print("Published successfully")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

client.connect("public.vantiq.cn", 1883, 60)
client.loop_start()

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
# client.loop_forever()
temperature = 0

while True: 
    # construct a json data
    now = datetime.datetime.now()
    timeString = now.strftime("%B %d, %Y")

    data = {
             'id':  1, \
             'temperature': temperature, \
             'time': timeString
           }

    s = json.dumps(data)
    client.publish("/xiaoguo/temperature", s)
    temperature += 1
    time.sleep(2)