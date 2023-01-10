# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster AS base

WORKDIR /app

# copy requirements into docker /app/requirements
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# copy everything into docker /app/requirements
COPY . .

CMD [ "python3", "-m" , "main"]