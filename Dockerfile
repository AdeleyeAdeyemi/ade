# Use lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY app.py .
COPY modules ./modules
COPY templates ./templates
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install gunicorn for production server
RUN pip install gunicorn

# Expose Flask port
EXPOSE 8777

# Run app with Gunicorn (4 workers)
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8777", "app:app"]




