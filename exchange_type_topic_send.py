#!/usr/bin/env python
import pika
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters( host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='topicexchangelogs',
                         exchange_type='topic')

topic = "error.warning.info"

for i in range(10000):
	send_str = 'index:{} Hello World!'.format(i)
	channel.basic_publish(exchange='topicexchangelogs',
	                      routing_key=topic,
	                      body=send_str)
	print(" [x] topic:{} Sent:{}".format(topic, send_str))
	time.sleep(1)

connection.close()