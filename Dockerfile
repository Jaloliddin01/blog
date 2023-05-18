FROM python:alpine
COPY . /app 
WORKDIR /app
CMD env\Scripts\activate; pip install -r requirements.txt; python manage.py runserver
