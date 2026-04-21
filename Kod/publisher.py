# ---------- Publisher 1 ----------
# Simulate IoT-data and publish to broker/HiveMQ

import time
import json
import random
import paho.mqtt.client as mqtt

# MQTT Broker
broker = "438919e0ee144402acc6dfb0d88dbd91.s1.eu.hivemq.cloud"
port = 8883
username = "testIOT"
password = "Password123"
topic = "room1/environment1"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.username_pw_set(username, password)

client.tls_set()

client.connect(broker, port, 60)
client.loop_start()

print("MQTT connected")

# Publish data


for i in range(20):
    chance = random.random()

    if chance < 0.75:
        sensor_data = round(random.uniform(18, 24), 1)
    elif chance < 0.95:
        sensor_data = round(random.uniform(25, 28), 1)
    else:
        sensor_data = round(random.uniform(29, 35), 1)



    data = {
        "device_id": "sensor_1",
        "temperature": sensor_data,
        "timestamp": time.time()
    }

    payload = json.dumps(data)
    result = client.publish(topic, payload)
    print("Sent:", data, "status:", result.rc)
    time.sleep(2)

client.loop_stop()
client.disconnect()
print("Publisher finished")