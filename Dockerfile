FROM python:3.9.7-slim

ENV PYTHONUNBUFFERED 1
ENV API_PORT 8000
ENV API_WORKER_COUNT 2
ENV PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.1


RUN apt-get update && \
    apt-get install -y --no-install-recommends netcat && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# System deps:
RUN pip install poetry==${POETRY_VERSION}} \
    tox

RUN mkdir /thrivey-api
WORKDIR /thrivey-api
COPY poetry.lock pyproject.toml /thrivey-api/

# Copy app dir
COPY . /thrivey-api

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

# API Port
EXPOSE 8000

# Run tox - test & build
RUN tox

RUN mkdir -p logs
RUN chmod u+x bin/*.sh

# Prep DB 
ENTRYPOINT [ "bin/run-api.sh" ]

# Run API
CMD [ "bin/prep-db.sh" ]
