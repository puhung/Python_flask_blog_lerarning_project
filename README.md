# Overview - Flask blog post website

This is a online course project for learning to build a Blog post website using Flask, Flask-SQLAlchemy, Flask-WTF.

## Table of contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Sources](#sources)

## Technologies

* Python 3.9.9
* Flask 1.0.2
* Flask-Login 0.4.1
* Flask-Migrate 2.1.1
* Flask-SQLAlchemy 2.3.2
* Flask-WTF 0.14.2
* Jinja2 2.10
* Werkzeug 0.14.1


## Setup
To run this project, download the project and create a virtual env in the downloaded file:

```
$ cd /path/to/this/project
$ python3 -m venv venv
$ source venv/bin/activate
```

After activating the project, pip install the required modules
```
$ pip3 install -r requirements.txt
```

Run the app
```
$ python3 app.py
```

## Features
* Allow users to login and create, update, or delete their own posts.
* Allow users to update their personal info images.
* Allow users to view every post

## Sources
This web application is inspired by Jose Portilla "[Python and Flask Bootcamp: Create Websites using Flask!](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/)" tutorial

## License

[MIT](https://choosealicense.com/licenses/mit/)