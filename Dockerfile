FROM python:3.10-slim-buster

WORKDIR /app

COPY app/requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app/ /app

EXPOSE 80

CMD [ "python", "app.py" ]