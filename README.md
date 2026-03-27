📌 Project: Secure Invoice / Billing Software
🔹 Overview

A secure invoice management system built using FastAPI with DevSecOps practices including authentication, PDF generation, and CI/CD deployment.

🔹 Features
Invoice CRUD APIs
JWT Authentication
PDF Invoice generation
Secure endpoints
CI/CD pipeline
🔹 Tech Stack
FastAPI
SQLite
SQLAlchemy
ReportLab
Docker
GitHub Actions
Render
🔹 API Endpoints
Method	Endpoint	Description
POST	/login	Get JWT token
POST	/invoice/	Create invoice
GET	/invoice/	Get all invoices
GET	/invoice/{id}/pdf	Download PDF
🔹 Workflow
User logs in
JWT token generated
User creates invoice
Invoice stored in DB
PDF generated
CI/CD pipeline deploys app
🔹 CI/CD Pipeline
Code push triggers pipeline
Bandit security scan runs
Docker image built
Image pushed to Docker Hub
Deployment triggered on Render
🔹 Deployment

Application deployed on:
👉 https://invoice-app-latest-ibt2.onrender.com/docs

🔹 Learning Outcomes
DevSecOps pipeline implementation
Secure API development
Docker & cloud deployment
CI/CD automation