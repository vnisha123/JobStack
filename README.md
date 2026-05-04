# Job Tracker API

A robust FastAPI-based backend service designed to help job seekers manage their applications. This project implements secure user authentication and a relational database to keep track of job listings on a per-user basis.

## Key Features
*   **Secure Authentication**: Fully implemented OAuth2 with JWT (JSON Web Tokens) for secure user sessions.
*   **Data Protection**:  Password hashing using **Argon2** and **Pwdlib**.
*   **Relational Database**: Managed One-to-Many relationships (User ↔ Jobs) using **SQLAlchemy**.
*   **Automatic Documentation**: Interactive API testing environment via **Swagger UI**
*   **Input Validation**:  **Pydantic**.

##  Tech Stack
*   **Language:** Python 3.x
*   **Framework:** FastAPI
*   **Database:** PostgreSQL (SQLAlchemy ORM)
*   **Security:** PyJWT, Pwdlib, Argon2
*   **Validation:** Pydantic v2

---

