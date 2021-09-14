import os
import numpy as np
from pyspark import SparkContext, SparkConf
import librosa

conf = SparkConf().setAppName("PreprocessAudio").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf)

def preprocess(path):
    # resample at 8000 Hz
    sr = 8000
    sampled_audio, sr = librosa.load('../data/audio/' + path, sr = sr)
    # adjust length
    sampled_audio = np.pad(sampled_audio, (0, sr*10-len(sampled_audio)), mode = 'constant')
    librosa.output.write_wav(path = '../data/preprocessed_audio/' + path, y = sampled_audio, sr = sr) 

def preprocess_audios():
    filepaths = os.listdir('../data/audio/')
    rdd = sc.parallelize(filepaths, len(filepaths)).foreach(preprocess)
if __name__ == '__main__':
    preprocess_audios()

