# 消费者
#!/usr/bin/env python
import pika
import logging

#logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='topicexchangelogs',
                         exchange_type='topic')

result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
print(queue_name)

bind_topic = "*.*.info"
channel.queue_bind(exchange='topicexchangelogs',
                   queue=queue_name,
                   routing_key = bind_topic)

print(' [*] Waiting for info. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(queue=queue_name,
					  on_message_callback=callback,
                      auto_ack=True)

channel.start_consuming()