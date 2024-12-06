# Dockerfile

# Using Python base image version 3.10
FROM python:3.10

# Upgrade pip
RUN pip install --upgrade pip

# Create working directory /app
WORKDIR /app

# Copy all project files to the working directory
COPY . /app

# Install project dependencies from requirements.txt
RUN pip install -r requirements.txt

# Set the command to run the project using uvicorn
CMD ["uvicorn", "config.main:app", "--host", "0.0.0.0", "--port", "80"]