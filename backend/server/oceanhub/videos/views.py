import logging

from flask import Blueprint, Response, jsonify
from kafka import KafkaConsumer

logger = logging.getLogger(__name__)
videos_blueprint = Blueprint('videos', __name__)
# Continuously listen to the connection and print messages as recieved


@videos_blueprint.route('/test')
def index():
    example_response = [{
        'id': 'example_id'
    }]
    return jsonify(example_response)


@videos_blueprint.route('/<string:video_id>/stream')
def stream(video_id):
    logger.info('Creating consumer.')
    consumer = KafkaConsumer(bootstrap_servers='kafka:9092',
                             auto_offset_reset='earliest',
                             consumer_timeout_ms=1000)
    logger.info('Consumer created successfully.')
    consumer.subscribe(['video-stream'])
    return Response(kafkastream(consumer),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


def kafkastream(consumer):
    for msg in consumer:
        logger.info(f'Offset: {msg.offset}')
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + msg.value + b'\r\n\r\n')
