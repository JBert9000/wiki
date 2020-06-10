# Wiki

Installation Instructions:

In case the package didn't come with the virtual environment with all the pre-installed packages:

    $ pip3 install virtualenv

    $ python3 -m virtualenv virtual

To activate the Virtual Environment while in the same directory:

    $ source virtual/bin/activate

If you're in the directory with manage.py:

    $ source ../virtual/bin/activate

To deactivate:

    $ deactivate

Here are the dependancies for this project:

    $ pip3 install django pillow django-crispy-forms django-simple-history django-summernote psycopg2 whitenoise

To run the server, go to the directory with 'manage.py' and type:

    $ python3 manage.py runserver

# Description

Here is a proof of concept for a wiki page I made in Django. Anyone can manipulate the database as a login is not required. It is designed in a way that once you click on the first picture, simple instructions are made where you can play with the functionality of this demo.

There should be a fox as the first wiki post. The description will have links to 2 other posts which also have descriptions themselves that guide a user through the functionality of this app.

Functions include:

- Creating, reading, updating, and deleting wiki posts. There are links in every post that show all times the links were updated. Uploading pictures is available to the user as well. I have disabled deleting posts for this demo so that the original posts will still be up in case someone accidentally deletes them.

- There is a search function which look through the current model and searches through all titles of the model. If a search didn't come back with anything, it displays a message asking the user if they want to create the post.

- The description includes markdown formatting via a 3rd party package called 'Django Summernote'.
