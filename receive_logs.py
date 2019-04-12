#coding=utf-8
#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

#当Consumer关闭连接时，这个queue要被deleted。可以加个exclusive的参数
result = channel.queue_declare(queue="", exclusive=True, auto_delete=True)
queue_name = result.method.queue

channel.queue_bind(queue=queue_name,
					exchange='logs',
                   )

print ' [*] Waiting for logs. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] %r" % (body,)

channel.basic_consume(queue=queue_name,
					on_message_callback=callback,
                    auto_ack=False)

channel.start_consuming()