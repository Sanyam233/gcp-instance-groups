FROM python:3.13-alpine

ARG SECRET_KEY
ARG DEV_ENV

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV SECRET_KEY=${SECRET_KEY}
ENV DEV_ENV=${DEV_ENV}

CMD ["gunicorn", "main:app", "--worker-class", "eventlet", "-w", "1", "-b", "0.0.0.0:8080", "--limit-request-field_size", "16384"]


