# Use an official Python runtime as a parent image
FROM python:3.12.4-slim-bullseye

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /github_visitor_info_admin

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000
EXPOSE 8000

# Use Gunicorn as the WSGI server
CMD ["gunicorn", "github_visitor_info_admin.wsgi:application", "--bind", "0.0.0.0:8000"]
