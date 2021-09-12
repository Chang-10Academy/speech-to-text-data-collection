from kafka import KafkaConsumer
from json import loads
import librosa
import random
import numpy as np
import logging

consumer = KafkaConsumer(
    'audiostore',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
    )

for message in consumer:
    message = message.value
    print('consumed: {} {} {}'.format(message['transcript'], message['sample_rate'], message['audio'][:10]))

    try:
        transcripts = open('../data/Transcripts.txt', 'a', encoding = "utf-8")
    except FileNotFoundError:
        logging.error('transcript file not found')
    filename = str(random.randint(1,10**12))
    transcripts.write("({}) : {}\n".format(filename, message['transcript']))
    transcripts.close()
    librosa.output.write_wav('../data/audio/{}.wav'.format(filename), np.array(message['audio']), message['sample_rate'])
    logging.info('consumed: {} {} {}'.format(message['transcript'], message['sample_rate'], message['audio'][:10]))
    
