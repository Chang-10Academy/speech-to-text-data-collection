from flask import Flask, render_template, request, redirect,jsonify
import json
from kafka import KafkaConsumer, KafkaProducer
from scipy.io.wavfile import read, write
import io
import wavio
import kafka
from kafka.admin import KafkaAdminClient,NewTopic
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

import kafka
from kafka.admin import KafkaAdminClient,NewTopic


TOPIC_NAME = 'audio'


producer = KafkaProducer(bootstrap_servers=["b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092",
    "b-2.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"],api_version = (0,10,1))

    
def audio_byte(audio):
    wave = wavio.read(audio)
    rate = wave.rate
    sampwidth = wave.sampwidth
    data = wave.data
    data = data.tolist()
    dic = {'data' : data, 'rate': rate, 'sampwidth': sampwidth}
    return dic

@app.route('/', methods=['GET','POST'])
def kafkaProducer():  
    if request.method == "GET":
        try:
            data_received = get_data()["data"]
        
        except:
            data_received = "Refresh the Page to load the Transcription"

        redis.incr('hits')
        return render_template('index1.html',
                                count=redis.incr('hits'),
                                data = data_received)

    if request.method == "POST":
        f = request.data
        print(type(f))
        # print(f)
        producer.send("audio",f)
        print('sent to producer')
            
        return 'Done'
        

def get_data():
    message1 = "Refresh the page to get the Translation"
    consumer = KafkaConsumer('topic0001',
                        group_id='my-group5',
                        bootstrap_servers=['localhost:9092'])
    messages = consumer.poll(timeout_ms=1000,max_records=1)

    for tp, mess in messages.items():
        message=mess[0]
        # print ("%s:%d:%d: key=%s value=%s" % (tp.topic, tp.partition,
        #                                     message.offset, message.key,
        #                                     json.loads(message.value)))

        message1 = json.loads(message.value)

    return message1
           

if __name__ == "__main__":
    app.run(debug=True, port = 5000)
