import random
import math
import pandas as pd

data_path = './data/preprocessed/'
path = './data/processed.csv'

cloud_data_path = '/mnt/10ac-batch-4/all-data/transcriptions/Amharic_transcriptions/Clean_Amharic.txt'
cloud_csv_file_data_path = '/mnt/10ac-batch-4/all-data/transcriptions/Chang_transcriptions_csv/processed.csv'
cloud_data_lake_path = '/mnt/10ac-batch-4/all-data/Chang/'


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


def get_text_corpus_csv(n):
    with open(data_path+'data_'+str(n)+'.txt') as f:
        contents = f.readlines()
        list_data = []
        for line in contents:
            list_text = {}
            list_text['origin_text_data'] = 'data_'+str(n)
            list_text["sentence"] = line
            
            list_data.append(list_text)


        f.close()

    return list_data


def cloud_get_text_corpus_to_csv():
    with open(cloud_data_path) as f:
        contents = f.readlines()
        list_data = []
        n = 0
        for line in contents:
            list_text = {}
            list_text["sentence"] = line
            list_data.append(list_text)
            print(f" Progress: {round((n*100)/len(contents),2)} %")
            n += 1


        f.close()

    return list_data


if __name__ == "__main__":
    
    # Change to 'True' if you're running this script on your local pc , and chage the below if statement to 'False'
    if (False):
        data_list = []
        big_list = []
        for n in range(9999):

            returned_list = get_text_corpus_csv(n)
            data_list.append(returned_list)
            print(f" Progress: {round((n*100)/9999,2)} %")
            
        print(len(data_list))
        for lis in data_list:
            for l in lis:
                big_list.append(l)
        

        df = pd.DataFrame.from_dict(big_list)
        df['id']=df.index 
        df.to_csv(path, index=False)


# Change to 'True' if you're running this script on the cloud (AWS), and chage the above if statement to 'False'
    elif (True):

        returned_list = cloud_get_text_corpus_to_csv()
        
        print(len(returned_list))
        
        df = pd.DataFrame.from_dict(returned_list)
        df['id']=df.index 
        df.to_csv(cloud_csv_file_data_path, index=False)