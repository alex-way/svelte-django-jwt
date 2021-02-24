# Svelte - Django - JWT

First off a quick disclaimer, I'm still relatively new to Svelte and front-end development in general.

## Getting Started

```bash

cd frontend
npm i
npm run dev &

---

cd backend
virtualenv venv
source ./venv/scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver &

```

## Todo

* Guard routes to redirect to login
* Add sample items to database
