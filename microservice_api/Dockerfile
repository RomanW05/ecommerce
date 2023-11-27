# Use an official Python runtime as a parent image
FROM python:3.10.13-slim

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY microservice_api/requirements.txt /app/


# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY microservice_api/. /app/


# Expose the port that the app will run on
EXPOSE 8000