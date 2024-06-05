from machine import Pin
import dht
import machine
import time

d = dht.DHT22(machine.Pin(4))
d.measure()
print('------Hello I am doing IoT------')
print(d.temperature())
d.temperature() # eg. 23 (°C)
d.humidity()    # eg. 41 (% RH)
#only once you run the d.measure() will the new values get
#updated on d.temperature
#so on console even if you run d.temperature after changing
#the temperature from the DHT22 GUI on simulation
#it will show the old value which was there before
#now on console run d.measure, then run d.temperature
#then it will show the new value that you put on DHT22 GUI