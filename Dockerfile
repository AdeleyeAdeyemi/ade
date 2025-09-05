FROM python:3.10-slim

WORKDIR /app
COPY app.py .
COPY modules ./modules
COPY templates ./templates


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


ENV ELK_HOST=logstash

EXPOSE 8777
CMD ["python", "app.py"]



