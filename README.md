# Note Management API

## Overview

This is a RESTful API for managing notes using Django and Django REST Framework (DRF). The API provides endpoints for creating, retrieving, updating, and querying notes. It also includes Swagger documentation for easy exploration of the API.

## Features

- **Create** a new note
- **Retrieve** a note by ID
- **Update** an existing note
- **Query** notes by title substring
- **Swagger UI** for API documentation

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/anantsaxena09/notes.git
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply database migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Access the API documentation:**

    Navigate to [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) in your web browser.

## Endpoints

- **POST** `/api/notes/` - Create a new note
- **GET** `/api/notes/` - List all notes
- **GET** `/api/notes/{id}/` - Retrieve a note by ID
- **PUT** `/api/notes/{id}/` - Update a note by ID
- **GET** `/api/notes/query/` - Query notes by title substring
