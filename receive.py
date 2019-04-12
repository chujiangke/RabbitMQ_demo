#coding=utf-8
import pika

#创建一个连接对象,对象中绑定了rabbitmq的IP
connection=pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
#创建一个频道对象
channel=connection.channel()
#频道中声明指定queue,如果MQ中没有指定queue就创建,如果有,则略过
channel.queue_declare(queue='cc')

#定义回调函数
def callback(ch,method,properties,body):
    print("ch:{}".format(ch))
    print("method:{}".format(method))
    print("properties:{}".format(properties))
    print("body:{}".format(body))
    print('[x] Recieved %r'%body)
    
# channel.close()
#no_ack=Fales:表示消费完以后不主动把状态通知rabbitmq,callback:回调函数,queue:指定队列
channel.basic_consume('hello', callback, True)
# channel.basic_consume(callback,queue='cc')
print('[*] Waiting for msg')
channel.start_consuming()
