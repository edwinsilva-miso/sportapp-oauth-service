# SportApp OAuth Service

## Description

This service performs the authentication and authorization process for a determined user

### Server URI

`http://127.0.0.1:5000`

### Endpoints

#### Token

Generate a new token given the username and password

- curl

```shell
curl --location 'http://127.0.0.1:5000/oauth/token' \
--header 'Content-Type: application/json' \
--data '{
  "username": "johndoe",
  "password": "mypass1"
}'
```
- Response

| HTTP Code | Description                     |
|-----------|---------------------------------|
| 200       | OK response with a Bearer token |
| 401       | Unauthorized                    |
| 500       | Internal server error           |

#### Alerts

Generate a new alert when an authenticated user is an **ORGANIZADOR**. Otherwise, returns a HTTP 401 Unauthorized error

- Curl 

```shell
curl --location 'http://127.0.0.1:5000/api/alerts' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer ${TOKEN}' \
--data '{
  "alert": "alert"  
}'
```

The `${TOKEN}` placeholder is the generated token from the previous service.

- Response

| HTTP Code | Description                                                |
|-----------|------------------------------------------------------------|
| 200       | OK response with the generated alert                       |
| 401       | Unauthorized when the user is different to **ORGANIZADOR** |
| 500       | Internal server error                                      |

### Roles allowed

| Role        | Allowed |
|-------------|---------|
| DEPORTISTA  | No      |
| ORGANIZADOR | Yes     |
| EMPRESA     | No      |

## Instalation

### Database

In order to configure the database, is required to create a new Postgresql instance via Docker Compose.

```shell
$ cd ~/location/sportapp-oauth-service
```

Then, execute the docker-compose command when Docker service is up:

```shell
$ docker-compose up -d postgres
```

After that, you can use any database GUI of your preference. Use this BD connection:

| Property | Value             |
|----------|-------------------|
| DB_HOST  | `localhost:5432`  |
| DB_USER  | `sport-app_user`  |
| DB_PASS  | `S3cret`          |
| DATABASE | `sport_app_auth`  |

#### Execution of DB scripts

In the directory /script of the root application, are the scripts to restore the database:

- [01_ddl_create_database.sql](scripts%2F01_ddl_create_database.sql)
- [02_app_role_202403151946.sql](scripts%2F02_app_role_202403151946.sql)
- [03_app_user_202403151946.sql](scripts%2F03_app_user_202403151946.sql)

The scripts are ordered by execution, so is required to run them according to this order.

## Message Queue

This project uses RabbitMQ for messagig queue. For this configuration you can run it via docker compose:

```shell
$ docker-compose up -d rabbitmq
```

| Property    | Value            |
|-------------|------------------|
| RABBIT_URL  | `localhost:5672` |
| RABBIT_USER | `admin`          |
| RABBIT_PASS | `admin`          |
| QUEUE_NAME  | `alertas`        |

## Project setup

After the database installation, is required to set up the project. You must be located in the project root:

```shell
$ cd ~/location/sportapp-oauth-service
```

### Virtual Env

As the project is writen on python, is required to install a new Virtual Environment. For that purpose, we must execute the command:

```shell
$ python -m virtualenv venv
```

After that, you may activate it:

```shell
$ source venv/bin/activate
```
On Windows, the activate command will be:

```shell
$ .\venv\Scripts\activate
```

### Install dependencies

After the creation of the virtual environment, you may install the requirements for the project.

The following commands are necessary for the installation:

```shell
$ python -m pip install --upgrade pip
$ pip install -r requirements.txt
```

## Run project

After that, the project must execute with the command:

```shell
$ python main.py
```

The output is pretty similar to the following. That means the server is up:

```
 * Serving Flask app 'src'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 726-021-831
```
