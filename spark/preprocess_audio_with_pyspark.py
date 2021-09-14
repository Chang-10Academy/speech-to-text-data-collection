import os
from pyspark import SparkContext, SparkConf
import librosa

conf = SparkConf().setAppName("PreprocessAudio").setMaster("local[*]")
sc = SparkContext.getOrCreate(conf)

def preprocess(path):
    # resample at 8000 Hz
    sampled_audio = librosa.load('../data/audio/' + path, sr = 8000)
    librosa.output.write_wav('../data/preprocessed_audio/' + path, sampled_audio, 8000) 

def preprocess_audios():
    filepaths = os.listdir('../data/audio/')
    rdd = sc.parallelize(filepaths, len(filepaths)).foreach(preprocess)