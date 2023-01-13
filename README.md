# Python with Flask

## 🔧 Pre-requisites

Before running the project, you must have the following tool installed on your machine: 
* [Python v3.11.0](https://www.python.org/downloads/release/python-3110/)

Also, you will need to clone the repository:

```bash
## Cloning the repository
git clone https://github.com/mateuseap/python-with-flask
## Entering the directory
cd python-with-flask
```
## 🚀 Project setup

### > Setting the environment variables

Create a file named ``.env`` and copy and past in it what is inside the ``.env.example`` file (create the ``.env`` file in the same place that ``.env.example`` file is localized). After that, you'll need to change de ``DATABASE_URL`` variable value and put in it the URL of your own database, following the given structure: 

```bash
## Database URL
postgresql://username:password@host:port/database_name
```

### > Running the app

You'll need to run the commands below:
```bash
## Creating a virtual environment
python -m venv env
.\env\Scripts\activate
## Upgrading the pip 
python -m pip install --upgrade pip
## Installing dependencies
pip install -r .\requirements.txt
## Running the app
python -m flask run
```

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view it in the browser.

### > Creating the database

First, you'll need to open up a ``Python`` interactive shell:

```bash
flask shell
```

The special shell above runs commands in the context of the ``Flask`` application, so that the ``Flask-SQLAlchemy`` functions called are connected to the application. After openning this shell, you'll just need write this in it to create the database:

```Python
from app import db, User
db.create_all()
exit()
```
