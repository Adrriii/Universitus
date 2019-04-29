FROM ubuntu

RUN apt update
RUN apt install python3 -y

WORKDIR /game
COPY game /game
COPY ansi2html.sh .

CMD PYTHONIOENCODING=utf-8 python3 main.py | sh ansi2html.sh
