FROM python:3.10

ENV PROJECT_ROOT /dice_emulator

RUN mkdir $PROJECT_ROOT
COPY . $PROJECT_ROOT
WORKDIR $PROJECT_ROOT

RUN pip install -r requirements.txt