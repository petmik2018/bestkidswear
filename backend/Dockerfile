FROM python:3.8.6

WORKDIR /usr/src/backend

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

#RUN apt-get update && apt-get install postgresql-dev gcc python3-dev musl-dev

RUN pip install --upgrade pip

COPY ./req.txt .

RUN pip install -r req.txt

COPY . .

ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]