FROM python:3.10.4

WORKDIR /altay

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . .

RUN pip install --upgrade pip
COPY ./requirements.txt /altay/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /altay/requirements.txt
