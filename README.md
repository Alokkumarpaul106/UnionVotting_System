# 🗳️ UnionVote API — Online Voting System

A secure online voting system REST API built with **Python, Django, and Django REST Framework**. This project provides user registration, email verification, candidate management, and voting-related API endpoints.

## 🚀 Project Overview

UnionVote API is designed to manage an online voting system where users can register, verify their email addresses, view candidates, and participate in voting according to the system's rules and permissions.

## 🛠️ Technologies Used

- Python
- Django
- Django REST Framework (DRF)
- SQLite / Django-supported database
- SMTP (Gmail)
- Email Verification
- Django REST Framework Permissions
- Git and GitHub

## ✨ Features

- Django project and application setup
- Database models for voting-related data
- Serializers for API data validation and conversion
- API views for registration and voting operations
- URL routing and endpoint configuration
- Custom API permissions
- User registration API
- Email verification using verification tokens
- SMTP email configuration using Gmail
- Candidate API
- Vote API
- Secure handling of environment variables

## 📁 Project Structure

```text
UnionVote_API/
│
├── API/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   ├── urls.py
│   └── ...
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── manage.py
├── .env
├── .gitignore
└── README.md
```

*Note: Adjust the folder names to match your actual project structure.*

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Alokkumarpaul106/UnionVote_API.git
cd UnionVote_API
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install django djangorestframework djangorestframework-simplejwt python-dotenv
```

Install any additional packages required by your project.

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password
```

Configure the SMTP settings in Django's `settings.py`. Use a Gmail App Password instead of your normal Gmail password.

**Important:** Never commit your `.env` file or expose email credentials on GitHub.

### 5. Apply database migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create an admin account

```bash
python manage.py createsuperuser
```

### 7. Run the development server

```bash
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

## 🔗 API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/api/register/` | Register a new user |
| GET | `/api/candidate/` | Retrieve candidate information |
| POST | `/api/candidate/` | Create a candidate, if permitted |
| GET | `/api/vote/` | Access vote records, subject to permissions |
| POST | `/api/vote/` | Submit a vote, subject to permissions |
| GET | `/api/verify-email/` | Verify an email using the UID and token |

The exact HTTP methods and permissions depend on your URL configuration, views, and ViewSets.

## 📧 Email Verification

The registration process generates a verification token using Django's `default_token_generator` and sends a verification link to the registered email address.

Example:

```text
http://127.0.0.1:8000/api/verify-email/?uid=<uid>&token=<token>
```

The verification endpoint checks the UID and token before verifying the user's email address.

For production deployment, replace the localhost URL with your actual HTTPS domain.

## 🔐 Security and Permissions

- Apply appropriate authentication and permissions to API endpoints.
- Restrict candidate creation and modification to authorized users.
- Prevent unauthorized users from accessing or modifying other users' votes.
- Validate email verification tokens on the server.
- Store SMTP credentials in environment variables.
- Use HTTPS in production.
- Apply appropriate API throttling and validation.
- Enforce voting eligibility and prevent duplicate voting on the server.

## 🧪 API Testing

You can test the endpoints using Postman or the Django REST Framework browsable API.

Test cases should include:

- Valid and invalid registration data
- Duplicate username or email
- Successful and failed email verification
- Valid and invalid verification tokens
- Candidate access and permission checks
- Unauthorized vote access
- Duplicate voting prevention

## 🎯 Learning Outcomes

Through this project, I practised:

- Django project and app architecture
- Database model design
- Serializers and request validation
- Function-based and class-based API views
- URL routing
- Authentication and permission handling
- SMTP email integration
- Token-based email verification
- Environment variable configuration
- REST API testing and debugging

## 👨‍💻 Developer

**Alok Kumar Paul**

GitHub: [Alokkumarpaul106](https://github.com/Alokkumarpaul106)

---

*This project is developed for learning and demonstrating Django REST API development and online voting system concepts.*
