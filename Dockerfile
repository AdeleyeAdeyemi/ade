FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl && rm -rf /var/lib/apt/lists/*

COPY app.py .
COPY requirements.txt .
COPY templates ./templates

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
