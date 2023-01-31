import json
from time import sleep
# from typing import Optional

# from bs4 import BeautifulSoup
from kafka import KafkaProducer
import random

# from json import loads


def connect_kafka_producer():
    _producer = None
    try:
        _producer = KafkaProducer(bootstrap_servers=['34.66.235.59:9092'], api_version=(0, 10))
    except Exception as ex:
        print('Exception while connecting Kafka')
        print(str(ex))
    finally:
        return _producer


def publish_message(producer_instance, topic_name, key, value):
    try:
        key_bytes = bytes(key, encoding='utf-8')
        value_bytes = bytes(value, encoding='utf-8')
        producer_instance.send(topic_name, key=key_bytes, value=value_bytes)
        producer_instance.flush()
        print('Message published successfully.')
    except Exception as ex:
        print('Exception in publishing message')
        print(str(ex))


if __name__ == '__main__':
    #print("I am here - just outside loop")
    # producer = KafkaProducer(bootstrap_servers=['192.168.0.7:9092'], api_version=(0, 10))
    producer = KafkaProducer(bootstrap_servers=['34.28.118.32:9094'], api_version=(0, 10))

    count = 0

    """for i in range(6):
        count = count + 1
        s = "Hello From Kafka - Python " + "Message no: " + str(count)
        #ack = producer.send('my-topic', json.dumps(s).encode('utf-8'))
        producer.send('my-topic', json.dumps(s).encode('utf-8'))
        sleep(5)"""

    """while(1==1):
        count = count + 1
        s = "Hello From Kafka - Python " + "Message no: " + str(count)
        # ack = producer.send('my-topic', json.dumps(s).encode('utf-8'))
        producer.send('my-topic', json.dumps(s).encode('utf-8'))
        sleep(0.2)"""
    #print("I am here - just outside loop")

    while (1 == 1):
        count = count + 1
        #print("I am here - just inside loop")
        #s = "Hello From Kafka - Python " + "Message no: " + str(count)
        s = {
              "v1": random.uniform(1, 10),
              "v2": random.uniform(1, 10),
              "v3": random.uniform(1, 10),
              "v4": random.uniform(1, 10),
              "id": count,
              "prediction": 0.00001
            }
        producer.send('my-second-topic', json.dumps(s).encode('utf-8'))
        print(s)
        sleep(0.2)

    if producer is not None:
        producer.close()
