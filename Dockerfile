FROM python:3.8
ADD . /data_collection
WORKDIR /data_collection/services
RUN pip install -r requirements.txt
CMD python app.py