# weigh-in

A multi-user web application providing simple weight tracking. Uses security by obscurity instead of registration/login.

Built with Flask and Postgres. Utilizes some common Flask extensions, including
Flask-SQLAlchemy and Flask-WTF.

Responsive layout created with Bootstrap 4, and a couple lines of JQuery.

Tested on Python 3.5.1

## Installation

```
$git clone git@github.com:bq1990/weigh-in.git

$cd weigh-in

$mkvirtualenv -p /usr/local/bin/python3 weigh-in

$pip install -r requirements.txt

$createdb weigh_in

$source setenv.sh

$python manage.py create_all

```

## Run development server

```
$python manage.py run --reload
```

Open http://localhost:5000 on your browser.

## Testing

```
$createdb weigh_in_test

$py.test --cov
```

