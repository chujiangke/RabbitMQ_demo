# 消费者
#!/usr/bin/env python
import pika
import logging

#logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='directexchangelogs',
                         exchange_type='direct')

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
print(queue_name)

channel.queue_bind(exchange='directexchangelogs',
                   queue=queue_name,
                   routing_key = "error")

print(' [*] Waiting for error. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(queue=queue_name,
					  on_message_callback=callback,
                      auto_ack=True)

channel.start_consuming()