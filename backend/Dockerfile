FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN pip install pip -U
RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev  -y

ADD requirements.txt /code/

RUN pip install -r requirements.txt
ADD . /code/
# RUN python3 /code/manage.py makemigrations shopping_cart
# RUN python3 /code/manage.py migrate
