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
The migrate command looks at the INSTALLED_APPS setting creates any necessary database tables accordings to the database settings2 