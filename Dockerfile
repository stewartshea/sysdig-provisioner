FROM williamyeh/ansible:alpine3

RUN pip install sdcclient
COPY sysdig/ /sysdig/
COPY ansible/ /ansible/
ADD entrypoint.sh .

RUN chmod g=u /etc/passwd

ENTRYPOINT [ "/entrypoint.sh" ]
 