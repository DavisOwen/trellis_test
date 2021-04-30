# Test User:

username = test_user
email = test_user@test.com
password = test

# Steps:

run `./manage.py runserver`

submit requests to http://localhost:8000/

auth/: POST - gets authentication token (use credentials for test user above

num_to_english/: GET - converts number query param to english

# Testing

run ./manage.py test
