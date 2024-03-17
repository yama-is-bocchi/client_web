FROM python:3.10.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
RUN mkdir /client_web
WORKDIR /client_web
ADD requirements.txt /client_web/
RUN pip install --upgrade pip && pip install -r requirements.txt