FROM python:3-alpine

WORKDIR /Scrabble

RUN apk update
RUN apk add git
RUN apk add bash

RUN git clone 

RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.main " ]