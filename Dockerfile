FROM williamyeh/ansible:alpine3

RUN pip install sdcclient
COPY sysdig/ /sysdig/
COPY ansible/ /ansible/
ADD entrypoint.sh .

RUN chmod g=u /etc/passwd

RUN chgrp -R 0 /sysdig && \
    chmod -R g=u /sysdig 

ENTRYPOINT [ "/entrypoint.sh" ]
 