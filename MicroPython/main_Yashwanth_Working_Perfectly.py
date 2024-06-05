import network
import dht
import machine
import time
from umqttsimple import MQTTClient

wlan = network.WLAN(network.STA_IF) # create station interface
wlan.active(True) # activate the interface
#wlan.connect('Wokwi-GUEST', '') # connect to an access point
wlan.connect('Rechnernetze','rnFIW625')

while not wlan.isconnected():
  print("not connected")
  time.sleep(0.1)

print("successfully connected")
print(wlan.ifconfig())
#time.sleep(60)

# initiate the dht22 instance
d = dht.DHT22(machine.Pin(2))
# initiate the mqtt broker instance
client = MQTTClient("your student ", "broker.hivemq.com")
# connect to the mqtt broker
client.connect()

while True:
  try:
    d.measure()
    temp = d.temperature()
    humidity = d.humidity()

    # publish sensor data to MQTT broker
    client.publish("M_IoT/Yash/temp", str(temp))
    client.publish("M_IoT/Yash/humi", str(humidity))

    print("published temp: ", temp)
    print("published humidity: ", humidity)
    time.sleep(60)

  except Exception as e:
    print("Failed to read DHT sensor data: ", str(e))
    time.sleep(3)
