# ticket-booking-system
1. Project Overview

This is a ticket booking system. The primary goal of this project is to learn how to structure a backend system using modern frameworks and deployment tools. Throughout the development process, I focused on learning:

Utilizing web frameworks (Django) to develop a project.

Understanding relational models and database structuring.

Implementing JWT for authentication and user verification.

Managing authorization and permissions using Django’s admin interface.

Using Redis and Celery for asynchronous task execution.

Testing API requests using Postman.

Transferring data from local to Docker volumes for local deployment and then from local to cloud for production deployment.

Automating deployment with GitHub Actions, Docker, and AWS.

2. Tech Stack

This project uses the following technologies:

Django – Backend framework

Traefik – Reverse proxy and load balancing

MySQL – Database management

Celery – Asynchronous task queue

Redis – Message broker for Celery

Docker – Containerization

GitHub Actions – CI/CD automation

AWS – Cloud hosting (EC2 for deployment)

3. Setup & Deployment

Locally:

To run the project locally:

# Start the server using Docker Compose
docker-compose up --build

Production:

Uses GitHub Actions, Docker Compose, and AWS for automated deployment.

The CI/CD pipeline automates error detection and deployment.

The application is deployed to an AWS EC2 instance.

4. Docker & AWS Usage

The application is containerized using Docker.

Docker images are built locally and pushed to AWS.

AWS EC2 hosts the deployed application.

Traefik is used for reverse proxy management.

5. GitHub Actions

The CI/CD pipeline includes:

Building and testing the Docker image.

Running automated tests.

Deploying the application to AWS.

6. Environment Variables

The project requires a .env file with necessary configurations. These include:

Database credentials (e.g., MySQL connection string)

Secret keys for Django authentication

Redis and Celery configurations

(Ensure sensitive data is not committed to GitHub.)

7. Usage

To make the application accessible, a domain name is recommended.

Since this is a personal learning project, the server is currently accessed via the EC2 instance’s public IP.

8. Troubleshooting

Common Issues & Fixes:

Configuration mismatches: Ensure environment variables are correctly set.

Networking issues: Check Docker network settings and AWS security groups.

Database connection errors: Ensure MySQL is running and accessible.

Understanding virtual machines: Learn about Docker containers vs. AWS EC2 instances.
