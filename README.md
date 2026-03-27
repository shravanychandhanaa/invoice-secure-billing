# 📌 Secure Invoice / Billing Software

## 🔹 Overview

A secure invoice management system built using **FastAPI** with
**DevSecOps practices**, including authentication, PDF generation, and
CI/CD deployment.

------------------------------------------------------------------------

## 🚀 Features

-   Invoice CRUD APIs\
-   JWT Authentication\
-   PDF Invoice Generation\
-   Secure Endpoints\
-   CI/CD Pipeline

------------------------------------------------------------------------

## 🛠 Tech Stack

-   **Backend:** FastAPI\
-   **Database:** SQLite, SQLAlchemy\
-   **PDF Generation:** ReportLab\
-   **Containerization:** Docker\
-   **CI/CD:** GitHub Actions\
-   **Deployment:** Render

------------------------------------------------------------------------

## 🔗 API Endpoints

  Method   Endpoint            Description
  -------- ------------------- ------------------
  POST     /login              Get JWT token
  POST     /invoice/           Create invoice
  GET      /invoice/           Get all invoices
  GET      /invoice/{id}/pdf   Download PDF

------------------------------------------------------------------------

## 🔄 Workflow

1.  User logs in\
2.  JWT token generated\
3.  User creates invoice\
4.  Invoice stored in database\
5.  PDF generated\
6.  CI/CD pipeline deploys application

------------------------------------------------------------------------

## ⚙️ CI/CD Pipeline

-   Code push triggers pipeline\
-   Bandit security scan runs\
-   Docker image built\
-   Image pushed to Docker Hub\
-   Deployment triggered on Render

------------------------------------------------------------------------

## 🌐 Deployment

Application deployed on:\
👉 https://invoice-app-latest-ibt2.onrender.com/docs

------------------------------------------------------------------------

## 📚 Learning Outcomes

-   DevSecOps pipeline implementation\
-   Secure API development\
-   Docker & cloud deployment\
-   CI/CD automation

------------------------------------------------------------------------

