FROM python:3.8
ADD . /front-end-service
WORKDIR /front-end-service
RUN pip install -r requirements.txt
CMD python wsgi.py
