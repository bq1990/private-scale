# weigh-in

Multi-user web application providing simple weight tracking. Uses security by
obscurity instead of registration/login.

Flask, Postgres

Tested on Python 3.5.1

## Installation

git clone git@github.com:bq1990/weigh-in.git

cd weigh-in

mkvirtualenv -p /usr/local/bin/python3 weigh-in

pip install -r requirements.txt

createdb weigh_in

source setenv.sh

python manage.py create_all

## Run development server

python manage.py run --reload

http://localhost:5000

## Testing

createdb weigh_in_test

py.test --cov


