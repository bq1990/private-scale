# weigh-in

Multi-user web application providing simple weight tracking. Uses security by
obscurity instead of registration/login.

Flask, Postgres

## Installation

git clone git@github.com:bq1990/weigh-in.git

<create venv>

pip install -r requirements.txt

createdb weigh_in

python manage.py create_all

source setenv.sh

python manage.py run --reload

## Tests

createdb weigh_in_test

py.test --cov


