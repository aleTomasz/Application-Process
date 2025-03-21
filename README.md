# 👨‍🏫 Application-Process

A Flask web application for displaying mentor and applicant data from a coding school database.

Application-Process is a Flask-based web application that displays information about mentors and applicants from a coding school database. The application provides search functionality by mentor's last name, city, or applicant's first name.

It serves as a simple data viewer built on top of a backend query layer (data_manager.py), which returns lists of dictionaries containing mentor and applicant information. The project focuses on filtering, routing, and rendering data dynamically using Jinja templates.

## 📚 Description

This application allows users to:

- View a list of mentors
- Filter mentors by **last name** or **city**
- Search for applicants by **first name** to retrieve their phone numbers

The app uses `Flask` as a web framework and `data_manager.py` to interact with the database.

## 🧰 Technologies Used

- Python
- Flask
- HTML / CSS (Jinja2 templating)
- PostgreSQL / SQLite (or another backend DB via `data_manager.py`)
- Jinja2 templating

## 🚀 Features

- Homepage with navigation
- Mentors page with:
  - Optional filters by city or last name
  - Dynamically generated list of unique cities
- Applicant phone lookup by first name
- Server-side rendering of templates

- ## 📦 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/aleTomasz/Application-Process.git
