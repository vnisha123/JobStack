# Job Tracker API

A robust FastAPI-based backend service designed to help job seekers manage their applications. This project implements secure user authentication and a relational database to keep track of job listings on a per-user basis.

## Key Features
*   **Secure Authentication**: Implemented secure user authenticantion using jwt tokens.
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

