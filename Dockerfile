FROM python:3.10-slim

WORKDIR /app

COPY app.py .
COPY modules ./modules
COPY templates ./templates
COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt

RUN pip install gunicorn

EXPOSE 8777

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8777", "app:app"]





