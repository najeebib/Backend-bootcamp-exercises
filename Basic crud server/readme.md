# FastAPI Student Management System

This project implements a FastAPI-based web application for managing students, including authentication and authorization functionalities. It provides endpoints for signing up, signing in, adding students, retrieving students, and filtering students by class.

## Project Structure

The project consists of the following modules and routes:

### Modules

- **`auth_model.py`:** Defines the Pydantic model for authentication.
- **`student_model.py`:** Defines the Pydantic model for representing student data.
- **`auth_functions.py`:** Contains functions related to authentication, including hashing passwords, generating JWT tokens, and verifying tokens.
- **`db_functions.py`:** Provides functions for loading and saving data from/to JSON files.

### Routes

- **`auth_route.py`:** Defines routes related to authentication, such as user sign-up and sign-in.
- **`student_route.py`:** Contains routes for managing student data, including retrieving students, adding students, and filtering students by class.

### Middleware

- **Logging Middleware (`log_req`):** Middleware to log incoming requests and their methods.

### Server

- **`server.py`:** Implements the FastAPI server and middleware for logging requests.

## How to Run

1. Start the FastAPI server using `uvicorn server:app --reload`.
2. Access the API documentation at `http://127.0.0.1:8000/docs` to interact with the available endpoints.

## Endpoints

- **Authentication Endpoints:**
  - `POST /auth/sign_up`: Sign up a new user.
  - `POST /auth/sign_in`: Sign in an existing user.

- **Student Management Endpoints:**
  - `GET /school/students`: Retrieve all students.
  - `GET /school/students/{id}`: Retrieve a specific student by ID.
  - `POST /school/students`: Add a new student.
  - `PUT /school/students/{id}`: Update student.
  - `DELETE /school/students/{id}`: Delete student.
  - `GET /school/class/{name}`: Retrieve students belonging to a specific class.

Each endpoint performs the necessary authentication and authorization checks before processing requests.

For more details, refer to the respective module and route files.

