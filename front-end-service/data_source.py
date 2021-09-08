import random

data_path = './data/preprocessed/'


def get_text_corpus(n):
    with open(data_path+'data_'+str(n)+'.txt') as f:
        contents = f.readlines()
        count = 0
        list_text = {}
        for line in contents:
            count +=1
            list_text['line'+str(count)] = line
            # break
        f.close()
        print(list_text)

    return {"text_corpus": list_text}


if __name__ == "__main__":
    n = random.randint(0,9999)
    print(get_text_corpus(n))