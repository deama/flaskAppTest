FROM python:3.6.9
WORKDIR /opt/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

ARG MYSQL_DB_TEST
ARG SECRET_KEY
ARG MYSQL_DB
ARG MYSQL_HOST
ARG MYSQL_PASSWORD
ARG MYSQL_USER

ENV MYSQL_DB_TEST=$MYSQL_DB_TEST
ENV SECRET_KEY $SECRET_KEY
ENV MYSQL_DB $MYSQL_DB
ENV MYSQL_HOST $MYSQL_HOST
ENV MYSQL_PASSWORD $MYSQL_PASSWORD
ENV MYSQL_USER $MYSQL_USER

RUN pytest --cov application/ --cov-report=html
RUN rm ./application/templates/coverage.html
RUN mv ./htmlcov/index.html ./application/templates/coverage.html
RUN rm -r ./htmlcov/ 

ENTRYPOINT /usr/local/bin/gunicorn --bind=0.0.0.0:5000 --worker-class eventlet -w 2 application:app
