FROM ubuntu

RUN apt update
RUN apt install python3 -y

WORKDIR /game
COPY game /game

CMD python3 main.py