# Student Management System

The Student Management System is a FastAPI-based Python application that allows users to manage student records stored in a JSON file. It provides endpoints to retrieve student information, add new students, and filter students by their classes.

## Modules

### `student.py`

Defines the `Student` class representing a student with attributes such as name, ID, age, and classes. It also provides methods to retrieve student information.

### `data_handler.py`

Contains the `DataHandler` class responsible for reading student data from and adding new students to a JSON file.

### `server.py`

Implements the FastAPI server with endpoints for handling student-related operations such as retrieving all students, fetching a student by ID, adding a new student, and filtering students by class.

## Usage

1. Start the FastAPI server by running `server.py`.
   ```bash
   uvicorn server:app --reload

## Endpoints
 - `GET /students`: Retrieves all students from the database.
 - `GET /students/{id}`: Retrieves a student by ID.
 - `POST /students`: Adds a new student to the database.
 - `GET /class/{name}`: Retrieves students belonging to a specific class.

![crud server diagram drawio](https://github.com/najeebib/Backend-bootcamp-exercises/assets/79699737/01609da9-76db-4f80-9e9b-c30ab1957d51)
