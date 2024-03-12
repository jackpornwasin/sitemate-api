## Getting Started

### Dependencies

- Setting up a virtual environment for python using pipenv
- Refer to Pipfile for all the dependencies

### Installing

- After cloned the repo please continue with following steps
- Here, you should already have pipenv, python 3.10, and pip installed in you systems 
- After the runserver command executed the APIs should callable at http://localhost:8000

```bash
pipenv install
python manage.py migrate
python manage.py runserver
```

### Run unit test

Launches and run all the unit test cases, with  `python manage.py test`