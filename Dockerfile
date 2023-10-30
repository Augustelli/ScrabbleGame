FROM python:3-alpine
LABEL authors="Augusto Mancuso"
EXPOSE 6379
RUN apk update
RUN apk add git
RUN apk add redis
RUN git clone https://github.com/um-computacion-tm/scrabble-2023-Augustelli.git
WORKDIR /scrabble-2023-Augustelli
RUN git checkout nuevoEnfoque
RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m game.main" ]