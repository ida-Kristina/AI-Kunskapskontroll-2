# ---------- Subscriber ----------
# Connect to HiveMQ Cloud and subscribe to your topic
# Note that MQTT is a real-time publish/subscribe-protocol

import paho.mqtt.client as mqtt
import json
import csv
import os

# MQTT Broker
broker = "438919e0ee144402acc6dfb0d88dbd91.s1.eu.hivemq.cloud"
port = 8883
username = "testIOT"
password = "Password123"
topic = "room1/environment1"

# CSV-file
filename = "iot_data.csv"

if not os.path.exists(filename):
    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["device_id", "temperature", "timestamp"])

# Write to CSV on message
def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())

    print("Received:", data)

    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            data["device_id"],
            data["temperature"],
            data["timestamp"]
        ])

# MQTT callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(topic)

# MQTT client
client = mqtt.Client()
client.username_pw_set(username, password)
client.tls_set()

client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port)

print("Listening for data...")

client.loop_forever()