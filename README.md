# ToDo-app-python

## Run applications

`docker-compose up -d`

3 separate docker containers will be created
1. Angular app running as frontend available on http://localhost:8080
2. Python Django application as backend listening on port 8000
   3. API available on http://localhost:8000/api/tutorials
   4. available methods GET, POST, PUT, DELETE
5. Postgres database listening on port 5432
6. Postman collection & environment json files can be imported to Postman to test backend API