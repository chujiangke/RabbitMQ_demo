# ######################### 生产者 #########################
#!/usr/bin/env python
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters( host='localhost'))

channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

for i in range(10000):
	send_str = 'Hello World! index:{}'.format(i)
	channel.basic_publish(exchange='logs',
	                      routing_key='',
	                      body=send_str)
	print(" [x] Sent :{}".format(send_str))
	time.sleep(1)

connection.close()