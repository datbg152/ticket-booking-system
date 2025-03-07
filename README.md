Ticket Booking System

📌 Project Overview

This is a ticket booking system. The primary goal of this project is to learn how to structure a backend system using modern frameworks and deployment tools. Throughout the development process, I focused on:

🏗 Utilizing Django as a web framework.

🔗 Designing relational database models in MySQL.

🔑 Implementing JWT authentication for user verification.

🔒 Managing authorization & permissions via Django Admin.

⚡ Using Redis & Celery for asynchronous task execution.

🛠 Testing APIs using Postman.

📦 Containerizing the application with Docker.

🚀 Deploying to AWS EC2 via Docker & GitHub Actions.

🛠 Tech Stack

This project uses the following technologies:

Backend: Django, Django REST Framework

Database: MySQL

Asynchronous Processing: Celery, Redis

Containerization: Docker, Docker Compose

Networking & Proxy: Traefik

CI/CD: GitHub Actions

Cloud Deployment: AWS EC2

🚀 Setup & Deployment

🔹 Running Locally:

To run the project locally using Docker Compose:

# Start the server
docker-compose up --build

🔹 Deployment to AWS:

Uses GitHub Actions, Docker Compose, and AWS for automated deployment.

The CI/CD pipeline automates testing, error detection, and deployment.

The application is deployed on an AWS EC2 instance.

📦 Docker & AWS Integration

The application is containerized using Docker.

Docker images are built locally and pushed to AWS.

EC2 hosts the deployed application.

Traefik handles reverse proxy and load balancing.

🔄 GitHub Actions (CI/CD Pipeline)

The CI/CD pipeline includes:

✅ Building & testing the Docker image

✅ Running automated tests

✅ Deploying the application to AWS

🔑 Environment Variables

The project requires a .env file with essential configurations:

# Example environment variables
SECRET_KEY=your_secret_key
DB_HOST=your_mysql_host
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
REDIS_URL=redis://redis:6379/0
CELERY_BROKER_URL=redis://redis:6379/0

📌 Note: Do not expose sensitive data in public repositories!

💻 Usage

A domain name is recommended for public access.

Since this is a personal learning project, the server is currently accessed via the EC2 instance’s public IP.

⚠️ Troubleshooting

Common Issues & Fixes:

❌ Configuration mismatches → Ensure .env variables are set correctly.
❌ Networking issues → Check Docker network settings & AWS security groups.
❌ Database connection errors → Ensure MySQL is running and accessible.
❌ Understanding virtual machines → Learn about Docker containers vs. AWS EC2 instances.

