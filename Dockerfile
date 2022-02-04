FROM python:3.8-slim as production

ENV PYTHONUNBUFFERED=1
WORKDIR /node/app/

RUN apt-get update && \
    apt-get install -y \
    bash \
    build-essential \
    gcc \
    libffi-dev \
    openssl \
    postgresql \
    libpq-dev

COPY collector/requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt

COPY collector/collector.py ./collector.py

EXPOSE 8001