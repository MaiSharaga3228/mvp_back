Startup:
```commandline
docker-compose build django
docker-compose up django
```

Для доступа к админке нужно создать админа с помощью команды
```commandline
docker-compose exec django python3 manage.py createsuperuser
```
и пройти по необходимым шагам
