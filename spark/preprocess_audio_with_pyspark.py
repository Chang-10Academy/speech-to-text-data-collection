import os
import numpy as np
from pyspark import SparkContext, SparkConf
import librosa

conf = SparkConf().setAppName("PreprocessAudio").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf)

def preprocess(path):
    # resample at 8000 Hz
    sampled_audio, sr = librosa.load('../data/audio/' + path, sr = 8000)
    librosa.output.write_wav(path = '../data/preprocessed_audio/' + path, y = sampled_audio, sr = 8000) 

def preprocess_audios():
    filepaths = os.listdir('../data/audio/')
    rdd = sc.parallelize(filepaths, len(filepaths)).foreach(preprocess)
if __name__ == '__main__':
    preprocess_audios()

