FROM python:3.8-slim-buster

RUN mkdir /container
COPY / /container

WORKDIR /container

RUN pip install -r requirements.txt

CMD ["python3", "manage.py", "runserver", "0.0.0.0"]

