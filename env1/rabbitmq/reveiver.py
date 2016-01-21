# -*- coding: UTF-8 -*-
import sys
import time

import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# channel.queue_declare(queue='hello',durable=True)

channel.exchange_declare(exchange='direct_logs', type='direct')
result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue
severities = sys.argv[1:]
if not severities :
    print >> sys.stderr, "Usage: %s [info] [warning] [error]" %\
                            (sys.argv[0],)
    sys.exit(1)
    
for severity in severities:
    channel.queue_bind(exchange='direct_logs', queue=queue_name, routing_key=severity)
print '[*] Waiting for logs. To exit press CTRL+C'
# channel.queue_bind(exchange='logs', queue=queue_name)

# print '[*] waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print "[x] received %r" % (body,)
    time.sleep(body.count('.'))
    print "[x] done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

# channel.basic_qos(prefetch_count=1)#同一时间点值处理一个message
# channel.basic_consume(callback, queue='hello')
channel.basic_consume(callback, queue=queue_name, no_ack=True)
channel.start_consuming()