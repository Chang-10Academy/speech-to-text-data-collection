from flask import Flask, render_template, request, redirect,jsonify
import json
import speech_recognition as sr
from flask_cors import CORS
from kafka import KafkaConsumer, KafkaProducer
from scipy.io.wavfile import read, write
import io
import wavio
import kafka
from kafka.admin import KafkaAdminClient,NewTopic
import random

app = Flask(__name__)

import kafka
from kafka.admin import KafkaAdminClient,NewTopic


# admin_client = KafkaAdminClient(bootstrap_servers=["b-1.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092",
# "b-2.demo-cluster-1.9q7lp7.c1.kafka.eu-west-1.amazonaws.com:9092"],
# client_id='d_id')

# topic_list = []
# topic_list.append(NewTopic(name="audio", num_partitions=1, replication_factor=2))
# admin_client.create_topics(new_topics=topic_list, validate_only=False)

TOPIC_NAME = 'audio'

# KAFKA_SERVER = ['kafka:29092','kafka:29092','kafka:39092']

# # producer = KafkaProducer(
# #     bootstrap_servers = KAFKA_SERVER,
# #     api_version = (0, 11, 15)
# # )
# producer = KafkaProducer(
#     bootstrap_servers = KAFKA_SERVER, api_version=(0,11,5)
# )
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
#         text =  "አገራችን ከአፍሪካም ሆነ ከሌሎች የአለም አገራት ጋር ያላትን አለም አቀፋዊ ግንኙነት ወደ ላቀ ደረጃ ያሸጋገረ ሆኗል በአገር ውስጥ አራት አለም ጀልባያውም የወረቀት"
        text = random.choice(open('/mnt/10ac-batch-4/all-data/transcriptions/Amharic_transcriptions/Clean_Amharic.txt').readlines())
        return render_template('index.html',data = text)

    if request.method == "POST":
        f = request.data
        print(type(f))
        # print(f)
        producer.send("audio",f)
        print('sent to producer')
            
        return 'Done'
        
        # f = request.files['audio_data']
        # with open('audio_file.wav', 'wb') as audio:
        #     f.save(audio)

        # aud = audio_byte('audio_file.wav')
        # aud = json.dumps(aud).encode('utf-8')
        # print (aud)
        #     # push data into INFERENCE TOPIC
        # producer.send(TOPIC_NAME, key = b'audio', value = aud)
        # producer.flush()
        # print("Sent to consumer")
        # return render_template('index.html',request = 'POST')

# def kafkaProducer():
#     # if request.method == 'POST':
#     #     print("Recieved Audio File")
#     #     file = request.files["audio_data"]
#     #     print('File from the POST request is: {}'.format(file))
#     # return render_template('index.html',request = 'POST')

#     # r=sr.Recognizer

#     # with sr.Microphone as source:	
#     #     audio = r.listen(source)
#     if request.method == "POST":
#         f = request.files['audio_data']
#         # with open("audio_file.wav", "wb") as file:
#         #     file.write(audio.get_wav_data())       #audio.frame_data()

#         # with open("audio_file.wav", "rb") as wavfile:
#         #     input_wav = wavfile.read()
#         with open('audio_file.wav', 'wb') as audio:
#             f.save(audio)

#         with open("audio_file.wav", "rb") as wavfile:
#             input_wav = wavfile.read()

#         rate, data = read(io.BytesIO(input_wav))
#         reversed_data = data[::-1]
#         bytes_wav = bytes()
#         byte_io = io.BytesIO(bytes_wav)
#         write(byte_io, rate, reversed_data)

#         output_wav = byte_io.read()
#             # push data into INFERENCE TOPIC
#         producer.send(TOPIC_NAME, input_wav)
#         producer.flush()
#         print("Sent to consumer")
#         return render_template('index.html',request = 'POST')


if __name__ == "__main__":
    app.run(debug=True, port = 5000)
