# Use the official Python image
FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /code

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project code
COPY . /code/

# Expose the port that Gunicorn will run on
EXPOSE 8000

# Command to start the Gunicorn server
CMD ["gunicorn", "parceradmin.wsgi:application", "--bind", "0.0.0.0:8000"]
