FROM python:3.9-slim-buster

COPY requirements.txt ./

RUN pip install -r requirements.txt

ENV BASE_DIR="/"

RUN mkdir ${BASE_DIR}/app_data


COPY ./data ${BASE_DIR}/app_data/data
COPY ./src ${BASE_DIR}/app_data/src
COPY ./test ${BASE_DIR}/app_data/test


WORKDIR	${BASE_DIR}/app_data

ENTRYPOINT python ${BASE_DIR}/app_data/src/app.py