# ######################### 生产者 #########################
#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters( host='localhost'))

channel = connection.channel()

channel.queue_declare(queue='hello')

for i in range(10000):
	send_str = 'Hello World! index:{}'.format(i)
	channel.basic_publish(exchange='',
	                      routing_key='hello',
	                      body=send_str)

	print(" [x] Sent :{}".format(send_str))
	time.sleep(1)

connection.close()