# 1. Content

- [1. Content](#1-content)
- [2. Installation](#2-installation)
  - [2.1. Docker](#21-docker)
  - [2.2. Local Env](#22-local-env)
- [3. Usage](#3-usage)
# 2. Installation
There are two ways to get it up:
1. Using Docker
2. Using your local env
## 2.1. Docker
Just install Docker and run:
```bash
docker compose-up
```
With this you have the system running on your machine in the port 8000. You also need to add a super user to access the admin.  
To do this just run
```bash
docker-compose run app python3 manage.py createsuperuser
```
And give the proper data.

## 2.2. Local Env
You will need various tools installed on your computer.  
First you must install pipenv.    
In macOS, any distro and WSL the easiest way is to use pipx
```bash
pipx install pipenv
```
Now that you have pipenv, install your dependencies using pipenv with the following command:
```bash
pipenv install
```
Now you need a DB, the project will work with sqlite out of the box.
Run:
```bash
piepnv run python manage.py migrate
```
Now I think you have everything to make this work, you only need to run the following command and it should run:
```bash
pipenv run python manage.py runserver
```
This will start a server at port 8000.
You also need a super user whic you can create using:
```bash
pipenv run python manage.py createsuperuser
```
# 3. Usage
The admin it's only needed for invalidating profile data so, if you want to start feeding the db you can go to the [documentation](http://localhost:8000/redoc) and start playing with it.  
To use the patch method its important to be logged in you; can get the proper token for the user in the django admin.