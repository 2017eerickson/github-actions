FROM python:3.11-slim

WORKDIR /the/workdir/path

COPY . .

RUN pip install --no-cache-dir pytest

CMD ["pytest"]

