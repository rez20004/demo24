FROM ubuntu:18.04
MAINTAINER REZA SOODIN rez20004@yahoo.co.uk

RUN apt-get update
RUN mkdir -p /myapp
COPY ..

RUN pip install -r requirements.txt
CMD python manage.py runserver
