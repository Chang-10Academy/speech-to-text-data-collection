import random
import math
import pandas as pd

data_path = './data/preprocessed/'
path = './data/processed.csv'

m = 0 # global variable

def get_text_corpus(n):
    with open(data_path+'data_'+str(n)+'.txt') as f:
        contents = f.readlines()
        count = 0
        list_text = {}
        for line in contents:
            count +=1
            list_text['line'+str(count)] = line
            break
        f.close()
        print(list_text)

    return {"text_corpus": list_text}


def get_text_corpus_csv(n, m):
    with open(data_path+'data_'+str(n)+'.txt') as f:
        contents = f.readlines()
        list_data = []
        for line in contents:
            list_text = {}
            list_text["id"] = m
            list_text['origin_text_data'] = 'data_'+str(n)
            list_text["sentence"] = line
            m +=1
            
            list_data.append(list_text)


        f.close()

    return list_data


if __name__ == "__main__":
    
    data_list = []
    big_list = []
    for n in range(9999):
        # m +=1
        returned_list = get_text_corpus_csv(n, m)
        data_list.append(returned_list)
        print(f" Progress: {round((n*100)/9999,2)} %")
        
    print(len(data_list))
    for lis in data_list:
        for l in lis:
            big_list.append(l)
    

    df = pd.DataFrame.from_dict(big_list) 
    df.to_csv(path, index=False)