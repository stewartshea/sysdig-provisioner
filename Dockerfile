FROM williamyeh/ansible:alpine3

RUN pip install sdcclient
ADD sysdig/ .
ADD ansible/ .
ADD entrypoint.sh .

ENTRYPOINT [ "/entrypoint.sh" ]
 