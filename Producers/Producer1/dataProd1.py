import os

def readData(path, start,end):
    allSentence = []
    for i in range(start,end):
        file = open(path+'\data_%i.txt'%i,encoding="utf8")
        sentences = file.readlines()
        allSentence.extend(sentences)
    return allSentence

# path = str(os.path.abspath(os.path.join('../../data/preprocessed')))
# # print(len(allSentence))
# readData(path,9999)
# print(len(allSentence))