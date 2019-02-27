FROM python:2.7-alpine3.8

RUN pip install sdcclient
ADD entrypoint.sh .

ENTRYPOINT [ "/entrypoint.sh" ]
 