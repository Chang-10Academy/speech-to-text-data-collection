import wave

# print(audioFile)
# print(audioByte)


def get_Audio():
    audioFile  = wave.open("sample.wav", "r")
    # audioFile  = wave.open("audioFIle.wav", "r")
    audioByte = audioFile.readframes(-1)
    # sample = str(audioByte)
    # return {
    #     "id": 1,
    #     "Audio": audioByte,
    # }
    
    return audioByte
    # return audioByte


if __name__ == "__main__":
    print(get_Audio())
