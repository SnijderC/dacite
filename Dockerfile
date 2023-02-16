ARG IMAGE=python:3.10
FROM $IMAGE
WORKDIR /app
COPY . /app
RUN pip install -e .[dev,freezegun]
CMD pytest tests 