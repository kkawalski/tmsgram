# tmsgram

## db
 - install docker (https://docs.docker.com/engine/install/ubuntu/)
 - docker run -e "POSTGRES_PASSWORD=postgres" -p "5435:5432" -d postgres:13-alpine
## env
 - python3 -m venv env
 - source env/bin/activate
 - pip install -r requirements.txt
## run
 - python manage.py migrate
 - python manage.py createsuperuser
 - python manage.py runserver