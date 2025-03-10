# Troubleshooting

### Common Issues & Fixes:
- **Database Connection Errors:** Verify MySQL is running and accessible.
- **Networking Issues:** Check Docker network settings & AWS security groups.
- **Configuration Mismatch:** Ensure `.env` variables are correctly set.
- **VM vs. Containers:** Understand the difference between AWS EC2 and Docker containers.

---

# Usage

### Domain Requirement:
- Recommended for public access.

### Access Method:
- Uses EC2 instance’s public IP for connectivity.

---

# Environment Variables

### Configuration File: `.env`
```
SECRET_KEY=your_secret_key
DB_HOST=your_mysql_host
DB_NAME=your_database_name
DB_USER=your_username
DB_PASSWORD=your_password
REDIS_URL=redis://redis:6379/0
CELERY_BROKER_URL=redis://redis:6379/0
```
**Note:** Do not expose sensitive data in public repositories.

---

# GitHub Actions

### CI/CD Workflow Includes:
- **Build:** Generates Docker image.
- **Test:** Runs automated tests.
- **Deploy:** Pushes the application to AWS.

---

# Docker & AWS Usage

- **Docker:** Containerizes the application.
- **AWS:** Hosts the application on EC2.
- **Traefik:** Manages reverse proxy and load balancing.

---

# Setup & Deployment

### Production Deployment:
**Tools Used:** GitHub Actions, Docker Compose, AWS EC2.  
**Process:**
1. Automates testing and error detection.
2. Deploys the application to AWS EC2.

### Local Deployment:
**Command:**
```
docker-compose up --build
```

---

# Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** MySQL
- **Task Queue:** Celery, Redis
- **Containerization:** Docker, Docker Compose
- **Networking:** Traefik
- **CI/CD:** GitHub Actions
- **Cloud Hosting:** AWS EC2

---

# Project Overview

### Ticket Booking System

### Description:
This is a ticket booking system designed to understand backend system structuring using modern frameworks and deployment tools.

### Key Learnings:
- **Framework:** Utilizing Django as a web framework.
- **Database:** Designing relational database models in MySQL.
- **Authentication:** Implementing JWT authentication for user verification.
- **Authorization:** Managing user permissions via Django Admin.
- **Asynchronous Tasks:** Using Redis & Celery for background processing.
- **API Testing:** Using Postman to test and monitor API requests.
- **Containerization:** Deploying the system using Docker.
- **Deployment:** Automating deployment with GitHub Actions & AWS EC2.

