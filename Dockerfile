FROM python:3

RUN mkdir -p /app

COPY *.py /app/

CMD [ "python", "/app/main.py" ]
