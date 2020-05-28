FROM python:3.7-alpine

COPY . /app

WORKDIR /app

RUN pip3 install -r requirements.txt

USER 1001
EXPOSE 5000
CMD ["python3", "/app/app.py"]
