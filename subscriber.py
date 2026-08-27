import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "sensor/temperature"


def on_connect(client, userdata, flags, reason_code, properties):
    print(f"connected: {reason_code}")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT)

client.loop_forever()
