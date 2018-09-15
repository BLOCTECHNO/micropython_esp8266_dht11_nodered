#time
import time
#dht11
import dht
#import mqtt library
from umqtt.simple import MQTTClient
#import in/out pin
from machine import Pin

# Received messages from subscriptions will be delivered to this callback
#def sub_cb(topic, msg):
#    print((topic, msg))

def send(t,h):
    server="192.168.43.170"
    c = MQTTClient("umqtt_client", server)
    #c.set_callback(sub_cb)
    c.connect()
    c.publish(b"meteo", b"t {0},h {1}".format(t,h))
    c.disconnect()


d=dht.DHT11(Pin(2))

while True:
    d.measure()
    t = d.temperature()
    h = d.humidity()
    send(t,h)
    time.sleep(10)
