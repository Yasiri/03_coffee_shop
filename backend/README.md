# Coffee Shop Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```bash
export FLASK_APP=api.py;
```

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## Tasks

### Setup Auth0

1. Create a new Auth0 Account ## yaser_nami
2. Select a unique tenant domain ## fsndcoffeeshop3
3. Create a new, single page web application ## CoffeeShopService
4. Create a new API
    - in API Settings:
        - Enable RBAC ## Done
        - Enable Add Permissions in the Access Token ## Done
5. Create new API permissions:
    - `get:drinks-detail`
    - `post:drinks`
    - `patch:drinks`
    - `delete:drinks`
6. Create new roles for: ## Done
    - Barista 
        - can `get:drinks-detail`
    - Manager
        - can perform all actions
7. Test your endpoints with [Postman](https://getpostman.com).  ## Done
    - Register 2 users - assign the Barista role to one and Manager role to the other. ## Done
    - Sign into each account and make note of the JWT. ## Done
    - Import the postman collection `./starter_code/backend/udacity-fsnd-udaspicelatte.postman_collection.json` 
    - Right-clicking the collection folder for barista and manager, navigate to the authorization tab, and including the JWT in the token field (you should have noted these JWTs). ## Done
    - Run the collection and correct any errors. ## Done
    - Export the collection overwriting the one we've included so that we have your proper JWTs during review! ## DONE

https://{{YOUR_DOMAIN}}/authorize?audience={{API_IDENTIFIER}}&response_type=token&client_id={{YOUR_CLIENT_ID}}&redirect_uri={{YOUR_CALLBACK_URI}}


## yasser6903 barista:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InItMXpwZjhHbDZRdDAtV0dpc2pITiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjb2ZmZWVzaG9wMy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkZmVlYjRmMmE3ODMwMDE5NjA0MGIxIiwiYXVkIjoiY29mZmVlU2hvcCIsImlhdCI6MTU5MjI5NDE3NCwiZXhwIjoxNTkyMzgwNTc0LCJhenAiOiJjSXQyVnR6bGxxZWhYN0J4Tml3R2l1Z2hTZ2RHM3RYayIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmRyaW5rcy1kZXRhaWwiXX0.CB9ATedIaoG1WQaMuiXZRs6UhcJv4ntK8IGYYepI9OUyPz4L3M-mICgNY1nVztbWIYXi3e1QFqF9NbnxHkjr1ninOCMokOTvdHz_BLI5ApkHLF4DdORbpsKbXcQKUsAgJQfFJgelT-meK9hs9trD3NVo7Q1rJgKGd_7NxuwZJ5FibUPaWFzsuUlAXnOjmMcjSnLMMyYpvAmRXUiDn3WnGODp4wzjLjCTaFSXEZAUMxsYeQYLOTfwDZJz4f-n0EB_REwAwXi2kWd0_mo0Q7qeJZLYxPkHjzLFF1yCuwHgXfbLiwe3aFNc27aWriKFrr8NPwrYMC8jf9q8w3KJIS4AsA4


## yaser_nami manager:
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InItMXpwZjhHbDZRdDAtV0dpc2pITiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRjb2ZmZWVzaG9wMy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWVkZmVlOWNmMmE3ODMwMDE5NjA0MDgyIiwiYXVkIjoiY29mZmVlU2hvcCIsImlhdCI6MTU5MjI5NDAyMSwiZXhwIjoxNTkyMzgwNDIxLCJhenAiOiJjSXQyVnR6bGxxZWhYN0J4Tml3R2l1Z2hTZ2RHM3RYayIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmRyaW5rcyIsImdldDpkcmlua3MtZGV0YWlsIiwicGF0Y2g6ZHJpbmtzIiwicG9zdDpkcmlua3MiXX0.ghx1K_RbF3yY9AQ--4ETmCeo9-x7gAbEk42Pkjc4mej7dB29LUlMrqOPR_U2jhckMa2sEi_sHY3Unzg6wX7dVBaclGaQb5KmdDeflXPKcCwwYG00SSoGKT_Q1V1IpruTndg2sJTrX3ePpt1FM_4-NF39-rKSKcxQTbNd_aqEm9n6SHE9ECJw-kRovIoecHpYQygaBJKFe5vRQfmjmYDSopXhM0lqBWFJtTQ_6yfcvoY5nwVNZlTfLKBbmQ0WOzUeIG2eb7EDZcHLQd40s4HrThQyqcOtC-CQBd1GbNZHtvpn8Jg1YCUF1Q6J6i9yyWpw_bG1C9j_4KxslZu9VjSfXA

### Implement The Server

There are `@TODO` comments throughout the `./backend/src`. We recommend tackling the files in order and from top to bottom:

1. `./src/auth/auth.py`
2. `./src/api.py`
