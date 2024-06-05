
# IoT Project - Yashwanth Pindi - s0590681

## 1. Introduction
The IoT project is used in order to create a smart temperature and humidity measurement system at your home. It can also monitor the outside climate conditions and can instantly give you an update as to what you can expect on the day. This is helpful in case of taking decisions about outdoor activities or to compare the outside conditions with that of inside.

## 2. Pictorial Representation
```
https://lucid.app/lucidchart/7e540f21-df85-49fa-9bad-a417b86fbee6/edit?viewport_loc=41%2C-138%2C1914%2C885%2C0_0&invitationId=inv_5a627474-d00c-4171-be29-9f831db53a80
```

![IoT Project](https://github.com/pyashwanth32/IoT_Berlin_Weather_usingMQTT-NodeRed-ESP32/blob/main/Pictures/Pictorial_Representation.png)

<img src="Pictorial_Representation.png" alt="isolated" width="800"/>

## 3. Working Video
The working video of the project can be found in the HTW Server. The link is below:
```
https://mediathek.htw-berlin.de/video/yashwanth-proitd-iot-project/a01e76ab8ee42fbe9f3e38818266ffd8
```
The Video can also be found in the WorkingVideo Folder:
```
https://github.com/pyashwanth32/IoT_Berlin_Weather_usingMQTT-NodeRed-ESP32/blob/main/WorkingVideo/Yashwanth_ProITD_IoT_Project.mp4
```

## 4. Overview

### 4.1 Monitoring Inside Environment
This IoT project is used to measure temperature and humidity using a DHT22 sensor connected to an ESP8266 microcontroller. The ESP8266 is programmed using microPython which is a language used for programming microcontrollers with python. 

The data is then published to a HIVEMQ broker and then the data is accessed using a Node Red flow that is then used to publish the analysed data into telegram. The data is then sent every 30 minutes so that there is a continuous tracking of the conditions inside the environment. There is also an audio button which outputs the current temperature continuously.

### 4.2 Monitoring Outside Environment
This IoT project also makes use of the temperature collected from an open-source weather broadcasting website called as https://home.openweathermap.org/ whose data is accessed using node red flow and publishes into a telegram bot and sends data whenever I need it.

### 4.3 Dashboard
The Dashboard is an user interface of Node-Red which has the current weather information displayed on a time series graph. It also contains a single grapth containing all the temperatures from the same main topic (M_IoT) so that one can compare the different temperature readings.

If one needs to change the temperature or humidity in order to check the system, there is a slider which can change the temperature being processed by Node-Red.

### 4.4 Emergency Alerts
Along with this, there is also a feature of an email notification whenever there is a fire emergency in the environment. Whenever the temperature goes higher than a certain limit, an email notification is sent so that they are alerted of an emergency situation. This email notification is sent every 2 minutes so that there is no overload on the email account which might lead to these emails marked as spam.

Along with that, there is an Audio on the Node-Red Dashboard which outputs the temperature whenever the temperature is more than the threshold.

```
https://home.openweathermap.org/
```

## 5. Components of the Project
1. Microcontroller: The ESP8266 is a low-cost Wi-Fi microchip, with built-in TCP/IP networking software, and microcontroller capability. It can be used for simple programming using micro Python. MicroPython is a lean and efficient implementation of the programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.
```
https://github.com/pyashwanth32/IoT_Berlin_Weather_usingMQTT-NodeRed-ESP32/blob/main/MicroPython/main_Yashwanth_Working_Perfectly.py
```

2. MQTT Broker: MQTT stands for Message Queuing Telemetry Transport. MQTT Broker is a messaging protocol designed for devices with high latency, low bandwidth and unreliable networks.

3. Node Red: Node-RED is a programming tool for wiring together hardware devices, APIs and online services. Node Red was used to subscribe to the MQTT Broker topic that had the data published from the microcontroller. This data is then processed to be sent to the Telegram bot user interface which gives continuous updates and suggestions based on the current conditions. Node-Red has also been included with a API that takes the climate updates from https://home.openweathermap.org/ and sends them to a Telegram bot so that one has access to the current climatic conditions.
```
https://github.com/pyashwanth32/IoT_Berlin_Weather_usingMQTT-NodeRed-ESP32/blob/main/Node-Red/Yashwanth_Pindi_Flow_Working_Perfectly.json
```
![Temperature and Humidity Measurement](https://github.com/pyashwanth32/IoT_Berlin_Weather_usingMQTT-NodeRed-ESP32/blob/main/Pictures/Temperature_Humidity_Data.png)

<img src="Temperature_Humidity_Data.png" alt="isolated" width="800"/>

4. Telegram: Telegram is a cloud-based, cross-platform instant messaging service for interacting with all the users. It also offers having telegram bots that run automated tasks on the app. Node-Red continuously processes and transmits the data to the Telegram bot. The data is the current temperature and humidity levels in the environment the ESP8266 Is present.

![Inside Environment Data](https://github.com/pyashwanth32/IoT_Berlin_Weather_usingMQTT-NodeRed-ESP32/blob/main/Pictures/Inside_Temperature_Humidity.png)

<img src="Inside_Temperature_Humidity.png" alt="isolated" width="800"/>

![Outside Environment Data](https://github.com/pyashwanth32/IoT_Berlin_Weather_usingMQTT-NodeRed-ESP32/blob/main/Pictures/Outside_Temperature_Humidity.png)

<img src="Outside_Temperature_Humidity.png" alt="isolated" width="800"/>


## 6. Use Cases
Alerts are a crucial part of automation, since you should not be continuously monitoring your systems to actively know what is happening. This IoT system has the capability of detecting any abnormal conditions in the environment that the DHT22 sensor and the ESP8266 is installed in. If in case the temperatures detected are out of the ordinary, the IoT system sends out an alarm stating that the current situation must be looked into. There is also an audio feature present which can output the current temperature values.

## 7. Uniqueness of the project
The uniqueness of the project is that if one has to go outside, they can request for a weather update from the telegram bot. This information can be about the current temperature, current humidity, overall cloudiness, humidity, pressure, wind speed, maximum and minimum temperatures and the overall weather forecast.  This will help them have an overall estimation of the current forecast and conditions. Along with that, in the Node-red dashboard, one can compare the temperature and the humidity difference between the room which is being monitored by the DHT22 sensor, and the outside temperature and humidities.
![Link to the Plot](https://github.com/pyashwanth32/IoT_Berlin_Weather_usingMQTT-NodeRed-ESP32/blob/main/Pictures/Berlin_Open_Weather.png)

<img src="Berlin_Open_Weather.png" alt="isolated" width="800"/>

## 8. Conclusion
IoT systems can be used for making our lives better for an extremely low cost. These systems provide an interface to monitor many different aspects of our environment with simple interfaces and affordable costs.

## 9. Bibliography
```
https://nodered.org/ 
https://www.youtube.com/watch?v=QDFONY4WOHw
https://nodered.org/docs/user-guide/context
https://core.telegram.org/bots/features
https://docs.micropython.org/en/latest/esp8266/quickref.html#dht-driver
https://docs.micropython.org/en/latest/esp8266/quickref.html#networking
https://www.hivemq.com/
https://randomnerdtutorials.com/node-red-send-email-notifications/
https://www.youtube.com/watch?v=qw3oKBp4rrQ
https://nodered.org/docs/user-guide/context
```

## 10. Acknowledgement
I would like to express my sincere thanks to my professor Dr. Alexander Huhn who helped me throughout the project to make it successful. I would also like to thank Anusha Suresh Akshintala for helping me with the Node-Red Dashboard and the audio. I would also like to thank my classmates who supported and clarified my doubts during the course.
