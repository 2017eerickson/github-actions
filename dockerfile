FROM python:3.11-slim
# why this docker image base?

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir pytest

RUN pip install pytest

CMD [ "pytest" ]