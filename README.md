# sloth-website
This is a repo for the new website we're building for The Language Sloth server on Discord.

# How to Run it

Make sure you you have Python ande NodeJS installed and run the following commands on your command console

# Create a virtual environment
(Depending on your Python installation, it might be python3, python3.8 etc)
```cmd
$ python -m venv venv
```

# Activate it
## Linux
```cmd
$ . venv/bin/activate
```
## Windows
```cmd
$ venv\Scripts\activate
```

# Install Python dependencies
```cmd
$ pip install -r requirements.txt
```

# Install NodeJS dependencies and run build
```cmd
$ cd jstools
$ npm install
$ npm run build
```

# Make SQLite and its alterations
```cmd
$ cd ..
$ python manage.py makemigrations
$ python manage.py migrate
```

# Go to the project's root folder and un server
```cmd
$ python manage.py runserver
```
