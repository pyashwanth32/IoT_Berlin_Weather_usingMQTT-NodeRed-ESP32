import dht
import machine
import time
import network
from umqtt.simple import MQTTClient

def connect():
    wlan = network.WLAN(network.STA_IF) #creating the station interface
    wlan.active(True) #activating the interface
    wlan.connect('Rechnernetze','rnFIW625')

    while not wlan.isconnected():
        print("not connected")
        time.sleep(0.1)

    print("successfully connected")
    print(wlan.ifconfig())
    time.sleep(3)
    
    # Defining the pin number to which the DHT22 sensor is connected
    dht_pin = 2
    # Create a DHT object
    dht_sensor = dht.DHT22(machine.Pin(dht_pin))

    # initiate the dht22 instance
    d = dht.DHT22(machine.Pin(2))
    # initiate the mqtt broker instance
    client = MQTTClient("your student ", "broker.hivemq.com")
    # connect to the mqtt broker
    client.connect()

# Function to read and print temperature and humidity
def read_dht_sensor():
    dht_sensor.measure()
    temp_celsius = dht_sensor.temperature()
    humidity = dht_sensor.humidity()

    print("Temperature: {:.2f} °C".format(temp_celsius))
    print("Humidity: {:.2f}%".format(humidity))
    
    # publish sensor data to MQTT broker
    client.publish("M_IoT/Yash/temp", str(temp))
    client.publish("M_IoT/Yash/humi", str(humidity))


connect()
# Main loop
while True:
    try:
        read_dht_sensor()
        time.sleep(30)  # Sleep for 2 seconds before taking the next reading
        
    except Exception as e:
        print("Failed to read DHT sensor data: ", str(e))
        time.sleep(3)