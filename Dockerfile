FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY bot.py /app/bot.py
COPY requirements.txt /app

WORKDIR /app
RUN pip install -r requirements.txt