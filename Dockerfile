# Use official Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only the necessary files first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED=1
# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]