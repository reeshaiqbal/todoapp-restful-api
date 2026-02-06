# Todo List App (DRF + Swagger)

## Overview

This is a Todo List application implemented in **Python** using **Django** and **Django REST Framework (DRF)**.  
**Swagger** is integrated to provide a user-friendly interface for testing API endpoints.  
CRUD operations are implemented using both **ViewSets** and **APIView**. 
APIs are implemented manually using APIView for full control.
Users can manage tasks via RESTful API endpoints, demonstrating clean, modular, and maintainable code.
SignUp and Login logic is also implemented using **Token Authentication**. 

---

## Features

### APIs made with ViewSets and routers:

- **POST Todo**: Create a new task with a title and completion status.
- **GET Todo**: Retrieve all tasks or individual tasks.
- **DELETE Todo**: Remove a task from the list.
- **PUT Todo**: Update the details of an existing task.
- **PATCH Todo**: Partially update the details of an existing task.

### APIs made with APIView manually:

- **POST Todo**: Create a new task with a title and completion status.
- **GET Todo**: Retrieve all tasks.
- **DELETE Todo**: Remove a task from the list.
- **PUT Todo**: Update the details of an existing task.

### SignUp API made with APIView:
- **Accepts** user registration data (username, email, password).
- **Validates** input using DRF serializers.
- **Creates** a new user using create_user().

### Login API made with APIView:
- **Accepts** credentials (username + password).
- **Authenticates** manually using authenticate().
- **Returns** an existing or new token for the user to access protected APIs.

---

## OOP Concepts Used

This project applies **Object-Oriented Programming (OOP)** principles for clean and maintainable code:

- **Class**
- **Object**
- **Instance Variable**
- **Methods**
- **Encapsulation**
