Django-1.9-Template
===================

Template for Django 1.9 (Python 3.5)

Installation
------------

This README will walk you through the essentials on getting Django running on your computer. To begin with, you will need
a version of Python. Django 1.9 supports Python 2.7, 3.4, and 3.5. The above framework will be using Python 3.5; I recommend
also using this version. When working on a Python project, one should always attempt to work within a virtual environment.
This prevents global changes on a system and makes it easy to identify what requirements are necessary to get a project up
and running. In particular, if you had two Django projects but they relied on different versions of a particular package,
setting up virtual environments means this won't introduce any complications.

To install Python 3.5, I would also recommend using [Miniconda](http://conda.pydata.org/miniconda.html). It comes with a
separate package manager (conda) and an easy means of aquiring a variety of different packages. These packages tend to be
scientific in nature, but still can provide a lot of functionality (perhaps we want to upload a dynamic Matplotlib depending
on user input). To create the virtual environment called `myenv`, enter the following into your shell of choice:

```
python -m venv myenv
```

If you are running Ubuntu or Debian, the above will not work (the writers made a mistake in the code) so instead use the
following workaround (manually install pip script and run it):

```
python -m venv --without-pip myenv
source myenv/bin/activate
curl https://bootstrap.pypa.io/get-pip.py | python
deactivate
```

Setup
-----

Great! We now have a functional virtual environment. Whenever you want to work within this environment, make sure to `source`
the activate script. When leaving the environment, simply call `deactivate` and you'll be back in your default environment
(or at the least the one you were in before you ran activate). For now, go ahead and just delete this. I personally prefer
my virtual environment to be a subdirectory inside my Django project, and setup the .gitignore file accordingly. Now we'll
pull down the template to begin working:

```
git clone https://github.com/Guru-Developers/Django-1.9-Template
mv Django-1.9-Template ${NAME_OF_PROJECT}
cd ${NAME_OF_PROJECT}
[Create virtual environment called "venv"]
source venv/bin/activate
```

Lastly, we make sure our requirements are up to date (this is why virtual environments are so important!) by running the
following command:

```
pip install -r requirements.txt
```

If at any point you decide you need to include another package in the project, or you're dying to include a feature that
relies on something else, make sure to include this in the requirements.txt file so others know what they also need to install.
Even better, perhaps consider running the following after you finish installing a package just to make sure you never forget
something:

```
pip freeze > requirements.txt
```

Configuration
-------------

In order for everything to begin working on your local machine, you will need to adjust the `conf/settings.py` file. Make
sure to NEVER include confidential information in this file! If you make a pull request and we notice this, we cannot accept
that request until you remove the information. Any variables that need to be set should be done once you've cloned the
project. As a safety precaution, I include the settings file in the .gitignore after the initial commit. If you make any
changes that others must also work on, let us know and we'll notify everyone working on the project.

It would be nice if we were to have private repositories so as not to worry about this (though many people argue you still
shouldn't include anything confidential even in this case), but, since we don't want to spend any unnecessary money, just
make sure to be careful.

A final Git configuration necessary would be to change your remote URL. That is, if you are using some upstream site to
host your content, make sure to adjust the pushes necessary after your initial cloning (and then verify):

```
git remote set-url origin https://github.com/USERNAME/OTHERREPOSITORY.git
git remote -v
```

Database
--------

I personally prefer using PostgreSQL database backend, as I feel it provides a lot of support for a variety of different
features (such as GeoLocation) while still residing towards the SQL we all know and love (similar to Oracle or MariaDB for
those who've used either). The only problem I have with it is that it can be a bit difficult to get running on a local
machine. The following is designed to be run if you use some Linux distro (I'm using Debian as of now), so if you happen
to be running Windows or Mac, make sure to look at how to go about installing in those cases.

First, install the necessary packages:

```
apt-get install postgresql postgresql-client
```

There are other recommended ones, but I'll just stick with the core essentials for now. Installing the above will create
a new user on your machine called `postgres` and you can log on by doing the following:

```
su
[Enter Password]
su - postgres
```
Next we will create a sample database and database user (you!) so that you can easily log in without having to switch
to the `postgres` user account. First, run the following:

```
psql
```

while you are the `postgres` user to enter the psql command prompt. Then create the database and user account (note you
only have to do this one time, and if the database/user does not happen to exist), making sure to replace `${}` with
what you actually want there:

```
CREATE USER ${USERNAME} WITH PASSWORD '${USER_PASSWORD}';
CREATE DATABASE ${DATABASE_NAME} OWNER ${USERNAME};
```

And, just for fun, make yourself superuser within psql as well:

```
ALTER USER ${USERNAME} WITH SUPERUSER;
```

If you used the same username as your shell, you can simply call `psql` once you exit out of root (<CTRL-D> a couple of
times), and otherwise repeat with `su - ${USERNAME}` and enter the password you entered. To connect to the database you
just created, run `psql ${DATABASE_NAME}`.

You may not be able to login depending on your authentication protocol. To fix this, go to
`/etc/postgresql/X.Y/main/pg_hba.conf` (where X.Y denote the version number) and modify and change the word `ident` or
`peer` to `trust` instead. Lastly, reload postgresql and try again:

```
/etc/init.d/postgresql reload
```

Running
-------

To run the given project on your machine, simply call the following command:

```
python manage.py runserver
```

This may or may not be a development version running (which makes certain components easier to check), but do your best to
make sure production ready code does run correctly before pushing to the master branch (if you happened to fork off and
create a separate branch, by all means, go crazy). You can do this by setting `DEBUG = False` in the configuration file.

Advanced
--------

There are a lot of other components involved with Django, and as such I will not run through them here. Things that are good
to know though:

* Fixtures (and now possibly Data Migrations)
* Migrations
* Middleware
* CSRF Security
* Serialization
* Django REST Framework
* Gunicorn
* WSGI

Don't worry if you don't know what some or all of these things are, and always feel free to ask any questions on how things
work. Chances are I forgot a lot of this as well, so it'll be good to be forced to relearn as much as possible anyways. Also,
make sure to look throughout the code as I'll try and document everything as much as possible.

Happy Coding!
