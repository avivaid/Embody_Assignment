# 
Embody_Assignment

## Developers

* [Aviral Vaid](https://github.com/avivaid)

## Getting started 
* [Install docker and docker-compose](https://docs.docker.com/get-docker/)
* Build the docker backedn contanier with the command 
``` docker-compose build backend ```
* Build the docker frontend contanier with the command 
``` docker-compose build frontend ```
* You can run the docker contanier as a bash shell with the command 
```docker-compose run contanier-name /bin/bash ``` or ```docker-compose run contanier-name bash ```
* Build the entire thing
  ** For some reason the npm packages are not getting installed in the docker container so before buliding the project install the frontend packages using npm. Follow the steps        below
  
      cd frontend

      npm install

      cd ..

      docker-compose up --build



* You might have to run migratiuions. 
```docker-compose run backend bash ```
```cd music_player ```
``` python manage.py makemigrations```
```python manage.py migrate ```



* You can bring up the container with the command 
```sudo docker-compose up ```
The backend django rest api can be accessed on loacalhost:8000 and the front react app can be accessed on localhost:3000

