# FastApi_Operation
Overview
This project is a basic CRUD API built with FastAPI. It uses an in-memory list as a fake database to demonstrate the core principles of creating, reading, updating, and deleting resources. The API endpoints are designed to handle common HTTP methods (POST, GET, PUT, DELETE). It uses Pydantic for data validation and serialization, ensuring the data received and returned by the API is well-structured.

Features
Create: Add a new item with a unique id and a name.

Read: Retrieve a single item by its id or get a list of all items.

Update: Modify an existing item based on its id.

Delete: Remove an item from the database using its id.

Getting Started
Prerequisites
You'll need Python 3.7+ installed on your system.

Installation
Clone this repository (or copy the code into a file named main.py).

Install the required packages:

Bash

pip install "fastapi[all]"
Running the API
To run the API, use the uvicorn server:

Bash

uvicorn main:app --reload
main: refers to the Python file main.py.

app: refers to the FastAPI instance created inside the file.

--reload: automatically reloads the server whenever you save changes to the code.

Once the server is running, you can access the interactive API documentation at:

http://127.0.0.1:8000/docs
This interface allows you to test all the API endpoints directly from your browser.
