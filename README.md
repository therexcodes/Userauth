
# User Authentication Project

A simple Django-based user authentication system that allows users to sign up, log in, and log out. Upon logging in, users are greeted with a personalized message displaying their first name on the home page.

---

## Features

- **User Signup**: Create a new account by entering user details.
- **User Login**: Access the platform with secure authentication.
- **Logout**: Log out securely from the session.
- **Personalized Greeting**: Logged-in users see a custom "Hello, [First Name]" message on the home page.

---

## Tech Stack

- **Backend Framework**: Django (v4.2.11)
- **Database**: PostgreSQL for secure and reliable data storage

---

## Prerequisites

Make sure you have the following installed:

- Python 3.8 or later
- PostgreSQL
- pip (Python package manager)

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/userauth.git
   cd userauth
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Database**
   - Ensure PostgreSQL is running.
   - Create a database named `userauth` (or any preferred name).
   - Update the `DATABASES` section in `settings.py`:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'userauth',
             'USER': 'your_postgres_user',
             'PASSWORD': 'your_postgres_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

5. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Open your browser and navigate to [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Dependencies

The project uses the following dependencies:

```
asgiref==3.8.1
dj-database-url==2.1.0
Django==4.2.11
gunicorn==22.0.0
packaging==24.0
psycopg2==2.9.9
psycopg2-binary==2.9.9
sqlparse==0.5.0
typing-extensions==4.11.0
tzdata==2024.1
```

---


## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements.

