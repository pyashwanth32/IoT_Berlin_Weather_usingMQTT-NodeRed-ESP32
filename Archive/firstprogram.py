import paho.mqtt.client as mqtt
brokerURL = "broker.hivemq.com"
brokerPort = 1883 # port number for unencrypted connections

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

def on_message(client, userdata, message):
    print("Received message '" + str(message.payload) + "' on topic '" + message.topic + "' with QoS " + str(message.qos))

def on_disconnect(client, userdata, rc):
    print("Client Got Disconnected")
    
mqttclient = mqtt.Client() #create client object

mqttclient.on_connect = on_connect
mqttclient.on_disconnect = on_disconnect
mqttclient.on_message = on_message

mqttclient.connect(brokerURL, brokerPort) #call connect function with URL and port number
mqttclient.subscribe("TestingTopic", qos=1)
mqttclient.loop_start()

mqttclient.publish(topic="M_IoT/681/test1", payload="I AM NOT ABLE TO SUBSCRIBE", qos=0, retain=True)
mqttclient.subscribe("M_IoT/+/test", qos=1)