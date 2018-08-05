import logging
import time

import cv2

from kafka import KafkaProducer

logger = logging.getLogger(__name__)


def video_emitter(video):
    # Open the video
    video = cv2.VideoCapture(video)
    logger.info(' emitting.....')
    #  connect to Kafka
    producer = KafkaProducer(bootstrap_servers='kafka:9092')
    # Assign a topic
    topic = 'video-stream'

    # read the file
    i = 0
    while (video.isOpened):
        # read the image in each frame
        success, image = video.read()
        # check if the file has read to the end
        if not success:
            break
        # convert the image jpg, lower quality for now
        # (we don't need to bloat the browser)
        encoding_param = [int(cv2.IMWRITE_JPEG_QUALITY), 70]
        ret, jpeg = cv2.imencode('.jpg', image, encoding_param)

        # Convert the image to bytes and send to kafka
        byte = jpeg.tobytes()
        producer.send(topic, byte)
        i += 1

        logger.info(f'bytesize {len(byte)}')
        logger.info(f'Frame No. {i}')
        # To reduce CPU usage create sleep time of 0.2sec
        time.sleep(0.2)
        # clear the capture
    video.release()
    producer.close()
    logger.info('done emitting')


def test_video():
    video_emitter('SampleVideo_1280x720_5mb.mp4')
