# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /app

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port for Cloud Run
EXPOSE 8080

# Start Django with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "backend.wsgi:application"]
