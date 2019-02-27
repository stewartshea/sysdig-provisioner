FROM williamyeh/ansible:alpine3

RUN pip install sdcclient
ADD entrypoint.sh .

ENTRYPOINT [ "/entrypoint.sh" ]
 