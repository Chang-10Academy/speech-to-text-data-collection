from flask import Flask, render_template, request, redirect,jsonify
import json
import speech_recognition as sr
from flask_cors import CORS
from kafka import KafkaConsumer, KafkaProducer
from scipy.io.wavfile import read, write
import io

app = Flask(__name__)

TOPIC_NAME = "audio"
KAFKA_SERVER = "localhost:29092"

producer = KafkaProducer(
    bootstrap_servers = KAFKA_SERVER,
    api_version = (0, 11, 15)
)


@app.route('/', methods=['GET','POST'])
def kafkaProducer():
    # if request.method == 'POST':
    #     print("Recieved Audio File")
    #     file = request.files["audio_data"]
    #     print('File from the POST request is: {}'.format(file))
    # return render_template('index.html',request = 'POST')

    # r=sr.Recognizer

    # with sr.Microphone as source:	
    #     audio = r.listen(source)
    if request.method == "POST":
        f = request.files['audio_data']
        # with open("audio_file.wav", "wb") as file:
        #     file.write(audio.get_wav_data())       #audio.frame_data()

        # with open("audio_file.wav", "rb") as wavfile:
        #     input_wav = wavfile.read()
        with open('audio_file.wav', 'wb') as audio:
            f.save(audio)

        with open("audio_file.wav", "rb") as wavfile:
            input_wav = wavfile.read()

        rate, data = read(io.BytesIO(input_wav))
        reversed_data = data[::-1]
        bytes_wav = bytes()
        byte_io = io.BytesIO(bytes_wav)
        write(byte_io, rate, reversed_data)

        output_wav = byte_io.read()
            # push data into INFERENCE TOPIC
        producer.send(TOPIC_NAME, input_wav)
        producer.flush()
        print("Sent to consumer")
        return render_template('index.html',request = 'POST')


if __name__ == "__main__":
    app.run(debug=True, port = 5000)
