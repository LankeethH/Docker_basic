# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy everything into the container
COPY . .

# Install packages
RUN pip install -r requirements.txt

# Run the app
CMD ["python", "app.py"]