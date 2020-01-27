FROM python:3.6.9
WORKDIR /opt/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

#RUN pytest

ENTRYPOINT /usr/local/bin/gunicorn --bind=0.0.0.0:5000 --worker-class eventlet -w 2 application:app
