FROM python:latest

ENV PROJECT_ROOT /app

RUN mkdir $PROJECT_ROOT

COPY . $PROJECT_ROOT

WORKDIR $PROJECT_ROOT

RUN pip install -r requirements.txt
RUN python setup.py install

CMD python src/dice_emulator/api.py
