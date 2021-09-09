import os
allSentence = []
def readData(path, numberoffile):
    for i in range(0,numberoffile):
        file = open(path+'\data_%i.txt'%i,encoding="utf8")
        sentences = file.readlines()
        allSentence.extend(sentences)
    return allSentence

path = str(os.path.abspath(os.path.join('../../data/preprocessed')))
# print(len(allSentence))
readData(path,9999)
print(len(allSentence))

# from utils.path import Path
# paths = Path()
# print(paths.getData)

