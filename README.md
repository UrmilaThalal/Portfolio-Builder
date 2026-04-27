# Portfolio Builder Backend

This is the backend for the Portfolio Builder project built using Django and Django REST Framework.
It provides basic API functionality and follows Test Driven Development (TDD) using pytest.

---

## Features

* Django backend setup
* Django REST Framework (DRF)
* Profile API (GET and POST)
* TDD using pytest

---

## API Endpoints

* **GET /api/profiles/** → Fetch all profiles
* **POST /api/profiles/** → Create a new profile

Example request:

```json
{
  "name": "John Doe",
  "bio": "Software Developer"
}
```

---

## How to Run

```bash
pip install django djangorestframework pytest pytest-django
python manage.py migrate
python manage.py runserver
```

---

## Run Tests

```bash
pytest
```

---

##  TDD Flow

* Wrote test first
* Test failed
* Implemented API
* Test passed

---

## Output

API runs at:
http://127.0.0.1:8000/api/profiles/

---

## Author
Urmila Thalal
