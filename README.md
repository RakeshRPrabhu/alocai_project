
# Alocai Game Challenge

Using Flask to build a Web Server with Swagger documentation.

Integration with Flask-SQLAlchemy, Marshmallow and Pytest extensions.

Added POSTMAN API Documentation in the file Alocai API Docs.postman_collection.json .


## Local Deployment Instructions

- Clone the repository and cd into directory:

```bash
   git clone https://github.com/RakeshRPrabhu/alocai_project.git
  
   cd services/
```

- Make sure that Docker and Docker Compose is installed on your system.

- Build the docker image using the following command:

```bash
   docker-compose build
```
- Once the image is built, run the container:

```bash
   docker-compose up -d
```

- Now Create the table using the below command

```bash
   docker-compose exec web python manage.py create_db
```

- Once this is done, go to the browser and fire up the localhost:5000/. You can use localhost:5000/docs to run each of the routes or use POSTMAN for the same.

- Lastly to run unit tests and functional tests use the following command:

```bash
   docker-compose exec web python -m  pytest "tests" -p no:warnings --cov
```
