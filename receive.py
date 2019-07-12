# ######################### 生产者 #########################
#!/usr/bin/env python
import pika
 
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
 
channel.queue_declare(queue='hello')
 
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
 
# 默认消息队列里的数据是按照顺序被消费者拿走，
# 例如：消费者1 去队列中获取 奇数 序列的任务，消费者1去队列中获取 偶数 序列的任务。
channel.basic_consume( queue='hello',
                       on_message_callback=callback)
 
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()