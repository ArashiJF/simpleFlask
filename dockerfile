FROM ubuntu:16.04

RUN mkdir /flaskapp

COPY ./requirements.txt /flaskapp

COPY ./hello.py /flaskapp

COPY ./templates /flaskapp/templates

RUN apt update -y

RUN apt -y install python3 python3-pip

RUN pip3 install --no-cache-dir -r /flaskapp/requirements.txt

WORKDIR /flaskapp

CMD ["python3", "hello.py"]
