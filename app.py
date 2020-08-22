import os
import csv

from datetime import datetime
from paho.mqtt.client import Client
from paho.mqtt import subscribe

mqtt_host = os.environ['MQTT_HOST']
mqtt_topics = 'sensors/#'

print('Listening for MQTT, topic={} host={}'.format(mqtt_topics, mqtt_host))

def handle_sensor_data(client, userdata, message):
  with open('data/' + message.topic.split('/')[1] + '.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow([int(datetime.now().timestamp()), float(message.payload)])

subscribe.callback(handle_sensor_data, mqtt_topics, hostname=mqtt_host)
