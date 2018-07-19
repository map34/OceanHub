from flask import Blueprint, Response
from kafka import KafkaConsumer

videos_blueprint = Blueprint('videos', __name__)
#Continuously listen to the connection and print messages as recieved

@videos_blueprint.route('/')
def index():
    consumer = KafkaConsumer(bootstrap_servers='kafka:9092',
                            auto_offset_reset='earliest',
                            consumer_timeout_ms=1000)
    consumer.subscribe(['video-stream'])
    return Response(kafkastream(consumer),
                        mimetype='multipart/x-mixed-replace; boundary=frame')

def kafkastream(consumer):
    for msg in consumer:
        # print(msg.value)
        # print(msg.offset)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + msg.value + b'\r\n\r\n')

