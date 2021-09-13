import os
import glob
import pandas as pd
import boto3
import logging
from botocore.exceptions import ClientError
import sys
import threading

text_path  = str(os.path.abspath(os.path.join('../data/preprocessed')))
csv_path = str(os.path.abspath(os.path.join('../data/text.csv')))
bucket_name = "chang-stt-bucket"
cloud_text_file_name = "chang-amharic-text-final.csv"



def readData(path, start,end):
    allSentence = []
    for i in range(start,end):
        file = open(path+'/data_%i.txt'%i,encoding="utf8")
        sentences = file.readlines()
        allSentence.extend(sentences)
    return allSentence

class TextDataServ:
    
    def __init__(self, textPath: str):
        self.textPath = textPath
        pass
    
    def get_file_length(self):
        os.chdir(self.textPath)
        return len(glob.glob("*.txt"))
          
    
    def creat_csv_text(self, csv_path =  str(os.path.abspath(os.path.join('../data/text.csv')))):
        total_file = self.get_file_length()
        sents = readData(self.textPath, 0, total_file)
        
        
        text_df = pd.DataFrame()
        text_df['text'] = sents
        text_df['length'] = text_df['text'].map(lambda x: len(x))
        
        file_names = [ f"data_{i}" for i in range(0, len(text_df['text'].to_list())) ]

        text_df['file_name'] = file_names
        text_df.to_csv(csv_path, index=False)
        text_df.head()
        text_df.info()
        print(len(file_names))
        
        
        return text_df
    
    def create_text_bucket(self, bucket_name="chang-stt-bucket", region=None):
        try:
            if region is None:
                s3_client = boto3.client('s3')
                s3_client.create_bucket(Bucket=bucket_name)
            else:
                s3_client = boto3.client('s3', region_name=region)
                location = {'LocationConstraint': region}
                s3_client.create_bucket(Bucket=bucket_name,
                                        CreateBucketConfiguration=location)
        except ClientError as e:
            logging.error(e)
            return False

    def upload_text_csv(self, csv_path: str, bucket: str, upload_file_name: str):

        
        s3_client = boto3.client('s3')
        
        print("transfering csv file to s3 bucket")
        
        try:
            with open(csv_path, "rb") as f:
                response = s3_client.upload_fileobj(f, bucket, upload_file_name,
                                                    Callback=ProgressPercentage(csv_path))
            
            print("Finished transfering csv file to s3 bucket")

        except ClientError as e:
            logging.error(e)
            return False
        
        return True
    
    def download_text_csv(self, csv_path: str, bucket: str, file_name: str):
        s3 = boto3.client('s3')
        try:
            with open(csv_path, 'wb') as f:
                   s3.download_fileobj(bucket, file_name, f)

            print("Finished downloading csv file from s3 bucket")
            return True

         
        except ClientError as e:
            logging.error(e)
            return False
        



class ProgressPercentage(object):

    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify, assume this is hooked up to a single filename
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()      

if __name__ == "__main__":
    text_serv = TextDataServ(text_path)
    text_serv.creat_csv_text(csv_path)
    text_serv.create_text_bucket(bucket_name)
    text_serv.upload_text_csv(csv_path, bucket_name, cloud_text_file_name)
#     text_serv.download_text_csv(csv_path, bucket_name, cloud_text_file_name)