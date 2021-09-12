import streamlit as st
import pandas as pd
import numpy as np
import base64
import pickle
import io
import logging
import scipy.io.wavfile as wavfile
import sounddevice as sd
import wavio
import librosa

from json import dumps
from kafka import KafkaProducer

def create_audio_player(audio_data, sample_rate):
    virtualfile = io.BytesIO()
    wavfile.write(virtualfile, rate=sample_rate, data=audio_data)
    return virtualfile

def main():
    st.title("Amharic Speech To Text Data Collection")

    st.sidebar.write("Navigation")
    app_mode = st.sidebar.selectbox("Choose Here", ("Home", "Record Audio"))
    if app_mode == 'Home':
        st.write('''
        ## Introduction
        Speech recognition technology allows for hands-free control of smartphones, speakers, and even vehicles in a 
        wide variety of languages. Companies have moved towards the goal of enabling machines to understand and respond 
        to more and more of our verbalized commands. There are many matured speech recognition systems available, 
        such as Google Assistant, Amazon Alexa, and Apple’s Siri. However, all of those voice assistants work for 
        limited languages only.
        
        Our responsibility was to build a deep learning model that is capable of transcribing a speech to text in the 
        Amharic language. The model we produce will be accurate and is robust against background noise.
        
        In order to make our model more accurate, we need more data. We would like to thank you for participating. Please navigate to the ''')

        logging.info("Homepage loaded")

    elif app_mode == "Record Audio":
        def record(duration, fs):
            sd.default.samplerate = fs
            sd.default.channels = 1
            myrecording = sd.rec(int(duration * fs))
            sd.wait(duration)
            return myrecording
        sample_rate = 8000
        st.subheader('Record a 10 second audio while reading out loud the text below')
        st.write('ይህም ትምህርት ቤቶች ከፖለቲካ ነፃ ከመሆናቸው አኳያ ሲከናወን የነበረው ተግባር ትክክል እንዳልነበር ገዢው ፓርቲም ለይቶ ገምግሞታል')
        if st.button(f"Start Recording"):
            myrecording = record(1, sample_rate)
            logging.info("recording complete")
            st.write("recording complete")
            #audios, predictions, transcripts = perform_predictions('./data/pred/')
            st.subheader('Your Audio')
            st.audio(create_audio_player(myrecording, sample_rate))
            wavio.write('audio.wav', myrecording, sample_rate, sampwidth=1)
        st.write("Click the send button to send the recorded audio")
        if st.button('Send'):
            producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                        value_serializer=lambda x: 
                                        dumps(x).encode('utf-8'))
            try:
                myrecording, _ = librosa.load('audio.wav')
            except FileNotFoundError:
                logging.error("audio file not found")
            producer.send('audiostore', value={"transcript": "ይህም ትምህርት ቤቶች ከፖለቲካ ነፃ ከመሆናቸው አኳያ ሲከናወን የነበረው ተግባር ትክክል እንዳልነበር ገዢው ፓርቲም ለይቶ ገምግሞታል", "sample_rate": sample_rate, "audio": list(map(lambda x:float(x), myrecording))})
            st.write("The audio has been sent. Thanks for your cooperation!!!")
            logging.info("Audio Sent")
if __name__ == "__main__":
    main()