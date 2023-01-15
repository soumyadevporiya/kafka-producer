import json
from time import sleep
# from typing import Optional

# from bs4 import BeautifulSoup
from kafka import KafkaProducer
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

    # producer = KafkaProducer(bootstrap_servers=['192.168.0.7:9092'], api_version=(0, 10))
    producer = KafkaProducer(bootstrap_servers=['my-cluster-kafka-bootstrap:9092'], api_version=(0, 10))

    for i in range(6):
        s = "Hello From Kafka - Python" + i
        ack = producer.send('test', json.dumps(s).encode('utf-8'))
        sleep(10)

    if producer is not None:
       producer.close()