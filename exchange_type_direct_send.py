#!/usr/bin/env python
import pika
import time
import random

connection = pika.BlockingConnection(pika.ConnectionParameters( host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='directexchangelogs',
                         exchange_type='direct')

routing_key_list = ["error", "warning", "info"]

for i in range(10000):
	send_str = 'index:{} Hello World!'.format(i)
	routingkey = random.choice(routing_key_list)
	print(routingkey)

	channel.basic_publish(exchange='directexchangelogs',
	                      routing_key=routingkey,
	                      body=send_str)
	print(" [x] routing_key:{} Sent:{}".format(routingkey, send_str))
	time.sleep(1)

connection.close()