FROM python:3.10-slim

WORKDIR /app

COPY app.py .
COPY Scores.txt .
COPY requirements.txt .
COPY templates ./templates

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["python", "app.py"]
