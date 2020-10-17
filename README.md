# Django Rest API

This is a small Django project to demonstrate Django CRUD functionality

* CRUD using FBV (Function Based Views).

## Install Required Packages

The Django CRUD project only need a single Python package "Django", it was built and tested with Django 3.x version. To install it use the following command:

```bash
pip install -r requirements.txt
```

Django 3 requires Python 3, if you need help setting up Python 3 on your machine you can consult DigitalOcean great documentation on [How To Install and Set Up a Local Programming Environment for Python 3](https://www.digitalocean.com/community/tutorial_series/how-to-install-and-set-up-a-local-programming-environment-for-python-3)


## Connect it to a Database

* Create the Database
* Create a separate MySQL user account that we will use exclusively to operate our new database.
* Add the MySQL Database Connection credentials in settings.py

## Running the Application

Before running the application we need to create the needed DB tables:

```bash
./manage.py migrate
```
Now you can run the development web server:

```bash
./manage.py runserver
```
## To run the test case:

```bash
./manage.py test
```
Test case consist of one positive and one negative test cases.

## To test the data from api
* CURL commands

```bash
curl -X POST -H "Content-Type:application/json" http://127.0.0.1:8000/team/create -d '{"firstname": "John","lastname": "Doe", "phonenumber": "1234567890", "email":"test@test.com","role": "True"}'


curl -X GET -H "Content-Type:application/json" http://127.0.0.1:8000/team/all -d'{}'


curl -X PUT -H "Content-Type:application/json" http://127.0.0.1:8000/team/update -d '{"id":"1","firstname":"Jack","phonenumber":"0987654321"}'


curl -X DELETE -H "Content-Type:application/json" http://127.0.0.1:8000/team/delete -d '{"id":"1"}'

```
