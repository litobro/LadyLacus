# Use official Python slim image for minimal footprint
FROM python:3.13-slim

# Set working directory
WORKDIR /app

# Install pip and gunicorn
RUN pip install --no-cache-dir gunicorn flask

# Copy app code
COPY . /app

# Install app dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port Flask/Gunicorn will run on
EXPOSE 8000

# Run the app with Gunicorn
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8000", "app:app"]
