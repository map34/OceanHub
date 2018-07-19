import time
import cv2
from kafka import KafkaProducer

def video_emitter(video):
    # Open the video
    video = cv2.VideoCapture(video)
    print(' emitting.....')
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
        # convert the image png
        ret, jpeg = cv2.imencode('.png', image)
        # Convert the image to bytes and send to kafka
        producer.send(topic, jpeg.tobytes())
        i += 1
        print('Frame No. %s' % i)
        # To reduce CPU usage create sleep time of 0.2sec
        time.sleep(0.2)
        # clear the capture
    video.release()
    producer.close()
    print('done emitting')

def test_video():
    video_emitter('SampleVideo_1280x720_5mb.mp4')
