# prepare Environment
## anaconda
- conda create -n name_env python=3.7
- conda activate name_env
- pip install -r requirement.txt

## virtualenv 
- virtualenv name_env
- source name_env/bin/activate
- pip install -r requirements.txt

## create database
### for sqlite 
- nothing to do

### for mysql
- create database orders
- modify the file maxo/settings.py
	- cancel commented-out code and comment other default code in DATABASE dict

## run the app
- python manage.py makemigrations
- python manage.py migrate
- python maxo/orders/data/import_data.py
- python manage.py runserver 0.0.0.0:8000 &

