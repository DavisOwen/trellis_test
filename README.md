# Test User:

username = test_user
email = test_user@test.com
password = test

# Steps:

`python3 -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

`./manage.py runserver`

# API

submit requests to http://localhost:8000/

auth/: POST - gets authentication token (use credentials for test user above)

request: {'username': <username>, 'password': <password>}

response: {'token': <token>}

num_to_english?number=<number>: GET - converts number query param to english

response: {'status': <status>, 'num_in_english': <num_in_english>}
error response: {'status': <status>, 'error': <error>}

# Testing

run ./manage.py test
