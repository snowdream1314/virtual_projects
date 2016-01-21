# -*- coding: UTF-8 -*-
import sys

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# channel.queue_declare(queue='hello',durable=True)
# channel.exchange_declare(exchange='logs', exchange_type='fanout')
channel.exchange_declare(exchange='direct_logs',type='direct')
severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "hello world!"
channel.basic_publish(exchange='direct_logs', routing_key=severity, body=message)
# message = ' '.join(sys.argv[1:]) or "hello world!"

# channel.basic_publish(exchange='', routing_key='hello', body=message, 
#                       properties=pika.BasicProperties(delivery_mode = 2,#make message persisitent
#                     ))
# channel.basic_publish(exchange='logs', routing_key='', body=message)
 
print "[x] sent %r" %(message,)

connection.close()