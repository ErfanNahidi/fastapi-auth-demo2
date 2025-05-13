**FastAPI Auth Demo 2**
A concise, production-oriented demonstration of authentication using FastAPI, JWT, and SQLAlchemy. Inspired by real-world security requirements and clean architecture principles.

---

## 📋 Table of Contents

1. [Overview](#overview)
2. [Features](#features)
3. [Tech Stack](#tech-stack)
4. [Prerequisites](#prerequisites)
5. [Installation](#installation)
6. [Configuration](#configuration)
7. [Running the Application](#running-the-application)
8. [Testing](#testing)
9. [Project Structure](#project-structure)
10. [Contributing](#contributing)
11. [License](#license)

---

## Overview

This project showcases a robust and minimal authentication service built with FastAPI. It covers user registration, login, secure password hashing, JWT token management, and dependency injection for high testability and modularity.

## Features

* **User Registration & Login**: Secure endpoints for creating accounts and authenticating users.
* **JWT-based Authentication**: Access and refresh tokens with configurable expiry.
* **Password Hashing**: Bcrypt-powered password storage.
* **Dependency Injection**: Clean separation of concerns using FastAPI's `Depends`.
* **SQLite Development DB**: Zero-configuration local database.
* **Scalable Structure**: Modular folders for routers, services, models, and schemas.

## Tech Stack

* **FastAPI**: High-performance web framework.
* **SQLAlchemy**: ORM for database interactions.
* **Pydantic**: Data validation and settings management.
* **JWT (PyJWT)**: Token creation and verification.
* **SQLite**: Lightweight embedded database.

## Prerequisites

* Python 3.10+
* Git
* pip (or poetry)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/ErfanNahidi/fastapi-auth-demo2.git
   cd fastapi-auth-demo2
   ```
2. **Create & Activate Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/macOS
   venv\\Scripts\\activate   # Windows
   ```
3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Rename `.env.example` to `.env` and update the following variables:

```dotenv
DATABASE_URL=sqlite:///./app.db            # Database connection string
SECRET_KEY=<your-very-secret-key>          # JWT signing secret (store securely!)
ACCESS_TOKEN_EXPIRE_MINUTES=30             # JWT access token validity
REFRESH_TOKEN_EXPIRE_MINUTES=43200         # JWT refresh token validity (30 days)
ALGORITHM=HS256                            # JWT algorithm
```

## Running the Application

1. **Initialize Database**

   ```bash
   alembic upgrade head   # Apply migrations (if using Alembic)
   ```
2. **Start FastAPI Server**

   ```bash
   uvicorn app.main:app --reload
   ```
3. **API Documentation**
   Open your browser and navigate to:

   * Swagger UI: `http://127.0.0.1:8000/docs`
   * ReDoc: `http://127.0.0.1:8000/redoc`

## Testing

Basic tests ensure endpoints behave as expected. To run the test suite:

```bash
pytest --cov=app tests/
```

## Project Structure

```
fastapi-auth-demo2/
├── app/
│   ├── main.py               # Application entrypoint
│   ├── routers/              # API route definitions
│   ├── services/             # Business logic and auth functions
│   ├── models/               # SQLAlchemy ORM models
│   ├── schemas/              # Pydantic schemas
│   └── core/                 # Settings and configuration
├── tests/                    # Test suite
├── requirements.txt
├── alembic/                  # Database migrations (optional)
└── README.md
```

## Contributing

Contributions are welcome. Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
