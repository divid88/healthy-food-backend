FROM python:latest

ENV PYTHONUNBUFFERD 1

WORKDIR /healthy

COPY requirements.txt /healthy/requirements.txt

RUN pip install -r requirements.txt

COPY . /healthy

CMD python manage.py runserver 0.0.0.0:8000