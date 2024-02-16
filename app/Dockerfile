FROM python:3.9.18

WORKDIR /app

RUN apt-get update && apt-get install -y unixodbc-dev

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app