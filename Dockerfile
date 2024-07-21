FROM python:3.10.14-slim-bullseye
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ADD . /app
CMD ["python", "/app/main.py"]
