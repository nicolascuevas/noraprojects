# Cornershop's backend test

- [Requirements](#Requirements)
- [Libraries](#Libraries)
- [Instructions](#Instructions)

## <a name="Requirements"></a>Requirements

- [HomeBrew](https://brew.sh/index_es)
- [Python 2.7](https://www.python.org/download/releases/2.7/)
- [VirtualEnv](https://github.com/pypa/virtualenv)
- [PyEnv + pyEnv-virtualEnv (optional)](https://github.com/pyenv/pyenv-virtualenv)
- [Redis](https://redis.io/)

## <a name="Libraries"></a>Libraries

- amqp v2.2.1
- billiard v3.5.0.3
- celery v4.0.2
- certifi v2017.4.17
- chardet v3.0.4
- Django v1.11.3
- django-appconf v1.0.2
- docutils v0.13.1
- idna v2.5
- kombu v4.0.2
- pytz v2017.2
- redis v2.10.5
- requests v2.18.1
- six v1.10.0
- slackclient v1.0.6
- urllib3 v1.21.1
- vine v1.1.4
- websocket-client v0.44.0

## <a name="Instructions"></a>Instructions

- Install HomeBrew
- Install pyenv + pyenv-virtualenv (Optional)
- Install virtualenv
- Install Redis (easier with HomeBrew)
- Clone the repository 


```bash
$ git clone git@github.com:xxxxxxxx/test-proj.git
```

- Setting virtualEnv inside repository folder

```bash
virtualenv venv
source venv/bin/activate
```

If you run ``which python`` or ``which pip`` you should see something like this: 
    
```
/YOUR_PATH/test-proj/venv/bin/python 
```

```
/YOUR_PATH/test-proj/venv/bin/pip 
```

- Install the required libraries

```bash
pip install -r requirements.txt
```

- Running migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

- Load initial "admin" user (Nora)

```bash
python manage.py meals/data/users.json
```

- Open two more terminal tabs or terminal windows (the first one will be used to run the app, the second one to run redis and the third one to run Celery)

- Run the app

```bash
python manage.py runserver
```

- Run redis

```bash
redis-server
```

- Run Celery

```bash
celery worker -A test-proj.celery_app --loglevel=DEBUG
```

## Tests

In order to run the tests and generate the coverage report you must run:

```bash
coverage run manage.py test meals  -v 2 && coverage html && open htmlcov/index.html
```

## Credentials

### Slack Space

- I'm assuming there's a channel where you, as an employee, can receive Nora's notifications so you will need to join the channel "almuerzos"

The notification is sent when you mark the checkbox "Send" when editing the menu itself (there must be some much better way for sure) and it says
``https://nora.cornershop.io/menu/SOME_UUID``, in order to see that page you need to manually replace ``https://nora.cornershop.io`` with
``http://localhost:8000``

### Nora

- Username: nora
- Password: cornershop
