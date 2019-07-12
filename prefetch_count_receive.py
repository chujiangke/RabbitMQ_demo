# ######################### 生产者 #########################
#!/usr/bin/env python
import pika
 
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
 
channel.queue_declare(queue='hello')
 
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

# prefetch_count在no_ask=false的情况下生效，即在自动应答的情况下这两个值是不生效的
channel.basic_qos(prefetch_count=1)

channel.basic_consume( queue='hello',
                       on_message_callback=callback,
                       auto_ack=True)
 
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()