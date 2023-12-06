# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Gunicorn
RUN pip install gunicorn

# Expose port 5000 for the Flask application
EXPOSE 5000

# Use Gunicorn to run the Flask application
ENTRYPOINT ["gunicorn", "flask_run5:app", "-b", "0.0.0.0:5000"]