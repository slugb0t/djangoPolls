# djangoPolls

create python environment and install dependencies
```bash
python venv env3
python install -r requirements.txt
```

Some of these applications make use of at least one database table, though, so we need to create the tables in the database before we can use them. To do that, run the following command:
```bash
python manage.py migrate
```
The migrate command looks at the INSTALLED_APPS setting creates any necessary database tables accordings to the database settings

On mysite/settings.py include the PollsConfig class
```python
NSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

migrate polls app
```bash
python manage.py makemigrations polls
```

Run python manage.py makemigrations to create migrations for those changes
Run python manage.py migrate to apply those changes to the database.



# Creating superuser
```bash
python manage.py createsuperuser
```



