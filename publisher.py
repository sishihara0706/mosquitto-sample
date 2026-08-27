import time
import random
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "sensor/temperature"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.connect(BROKER, PORT)

while True:
    temperature = round(random.uniform(20.0, 30.0), 1)

    client.publish(TOPIC, temperature)

    print(f"publish: {TOPIC} = {temperature}")

    time.sleep(2)
