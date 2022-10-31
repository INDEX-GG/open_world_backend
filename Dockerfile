FROM python:3.10.4

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /altay

RUN pip install --upgrade pip

COPY ./requirements.txt /altay/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /altay/requirements.txt

COPY . /altay/