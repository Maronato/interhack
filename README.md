# ALES's Website
Website that serves as a database and framework for the ALES Project

# Instructions to run locally

## Setting up

1. [Install Python 3](https://www.python.org/downloads/)
2. [Install virtualenv](https://virtualenv.pypa.io/en/stable/) (Accomplish this by running `pip3 install virtualenv`)
3. [Install Postgres](https://devcenter.heroku.com/articles/heroku-postgresql#local-setup)
4. Open a terminal window at the project's root:
 1. `virtualenv -p python3 venv` to create a virtual machine for the website
 * `source venv/bin/activate` to activate the virtual machine
 * `pip install -r requirements.txt` to install the requirements
 * `python manage.py migrate` to migrate the database
 * `python manage.py createsuperuser` to create the website's admin. Take note of the username and password for later
 * `python manage.py collectstatic` to collect the staticfiles so that the app is self-contained

 You can now start the server with `python manage.py runserver`, but follow the local instructions below first to set your environment variables.

## Local settings

You can modify the settings directly or create a `.env` to keep your local settings secret.

To use a `.env` simply create a new `.env` file at the root of the project and write the settings that you wish to alter, followed by their content.

A typical `.env` for this project should look like this (some settings may be missing):
```
EMAIL_PASSWORD=supersecretpassword
EMAIL_ACCOUNT=youremailaccount@domain.com
DJANGO_SECRET=longstringofrandomcharacters
EMAIL_ADMIN=adminaddress@important.com
SITE_URL=http://localhost:8000
```

If you wish, just go to `project/settings.py` and manually change the settings

*Don't forget to erase your passwords before pushing changes, though!*

### General settings
`SECRET_KEY` Django's signing key. No need to change it if running with `DEBUG = True`

`SITE_URL` is the website's domain. If running locally, yours wil probably be something like `http://localhost:8000`

### Email settings
To properly sign users in the website uses a email verification system.

You'll need a valid email account to serve as host

`DEFAULT_FROM_EMAIL` the default email address to be used as 'from' field

`EMAIL_HOST_USER` email address that'll be used as host

`EMAIL_HOST_PASSWORD` the password of the above host

You can leave `EMAIL_USE_TLS`, `EMAIL_HOST` and `EMAIL_PORT` as is if you are using gmail

`SERVER_EMAIL` the email address that django will use when sending error reports

`ADMINS` List of tuples with admin names and emails. Used when sending error reports

Now you are all set.

To start the website, do `python manage.py runserver`

# Using the website

Start by going to the index page and clicking Login

Use your admin username and password to login

Now you'll see some options. Start at the top and create a City.

Proceed by creating schools, courses, etc. Create as many as you want.

Whenever you create a Teacher or a Student, a confirmation email is sent to them. Within it you'll find a unique confirmation url. Use it to activate and set a password for the teacher or student.

You'll now be able to login as the activated teacher or student and do some other things as them, like enroll in courses or create events.
