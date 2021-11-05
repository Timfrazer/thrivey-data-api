FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED 1
ENV API_PORT 8000
ENV API_WORKER_COUNT 2

EXPOSE 8000
WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY poetry.lock pyproject.toml ./
RUN pip install poetry==1.1 tox

COPY . ./

RUN tox
    

RUN chmod u+x bin/*.sh

ENTRYPOINT [ "bin/prep-db.sh" ]

CMD [ "bin/run-api.sh" ]
