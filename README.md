# Data Engineering: Speech-to-text data collection with Kafka, Airflow, and Spark
## Introduction
In a previous project, we had trained a deep learning model that transcribes speech to text. The performance
of the model was mediocre because the size of the dataset was small. In this project, we are planning to use
Kafka, Spark, and Airflow to collect sufficient amount of data to improve the performance of the model.

## Code
So far, we have implemented a **kafka** producer, consumer and two types of web apps, one with html + javascript located in the **web-application** directory and another with streamlit, located in the **dashboard** directory. when users open the web app, they are shown randomly chosen amharic text. The users then record themselves while reading the amharic text out loud. The amharic text, along with the recorded audio is then sent to a kafka broker. The **consumer** then retrieves the text + audio one at a time, generates a random number as name for each, saves the text in the **data/Transcripts.txt** file, and it also saves the audio as a **.wav** file in the **data/audio** directory.

## Instructions
### streamlit web app 
To run the streamlit web app (the one that records audio), navigate to the dashboard folder, and execute the code below
```
pip install -r requirements.txt
streamlit run dashboard.py
```
### Running the producer and consumer
After starting your Zookeeper server and Kafka broker, navigate to the **scripts** folder and execute the code below

```
kafka-topics.bat --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic audiostore
```

Open two command prompt windows. On the first one, execute the following command to run the producer

```
python producer.py
```
On the second one, execute the following command to run the kafka consumer

```
python consumer.py
```

### Running the pyspark script to preprocess the audio files

```
cd spark
spark-submit preprocess_audio_with_pyspark.py
```