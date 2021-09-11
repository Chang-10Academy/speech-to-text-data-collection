FROM python:3.8
ADD . /speech-to-text-data-collection
WORKDIR /speech-to-text-data-collection/services
RUN pip install -r requirements.txt
CMD python app.py