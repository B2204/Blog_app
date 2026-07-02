# Django Blog CRUD Application

## Overview

This is a simple Blog CRUD (Create, Read, Update, Delete) web application built using Django. The project demonstrates the core concepts of Django, including models, views, templates, forms, URL routing, and the Django ORM.

## Features

- View all blog posts
- View a single blog post
- Create a new blog post
- Update an existing blog post
- Delete a blog post
- Django Admin Panel
- SQLite Database
- Bootstrap-ready template structure

## Technologies Used

- Python
- Django
- SQLite
- HTML
- CSS

## Project Structure

```
blog_project/
│
├── blog/
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
│
├── templates/
│   ├── base.html
│   └── blog/
│       ├── home.html
│       ├── detail.html
│       ├── create.html
│       ├── update.html
│       └── delete.html
│
├── db.sqlite3
├── manage.py
└── blog_project/
```

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Move into the project folder

```bash
cd blog_project
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install django
```

### Apply migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create an admin account

```bash
python manage.py createsuperuser
```

### Run the development server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

## CRUD Operations

- Create a blog post
- Read all blog posts
- View post details
- Update a blog post
- Delete a blog post

## Django Concepts Covered

- Django Project Structure
- Django Apps
- Models
- Django ORM
- Views
- URL Routing
- Templates
- Template Inheritance
- Forms
- ModelForm
- CSRF Protection
- Django Admin
- CRUD Operations
- SQLite Database

## Future Improvements

- User Authentication
- Comments
- Image Upload
- Search
- Pagination
- Categories
- REST API using Django REST Framework

## Author

Barathrajan Selvaraju