https://wikipage.herokuapp.com/wiki/ 

# Wiki

Here is a proof of concept for a wiki page I made in Django. Anyone can manipulate the database as a login is not required.

There is a 'Demo' section which uses static images from the Django / Heroku backend. The data is seeded directly through JSON written in the wiki/views.py file. The text data is stored in a Postgres database on Heroku's servers, while the image/gif uploads are handled by AWS S3.

Functions include:

- Creating, reading, updating, and deleting wiki posts. Each wiki post creates a link that shows every time that post was updated.

- There is a search function which look through the current model and searches through all titles of the model. If a search didn't come back with anything, it displays a message asking the user if they want to create the post.

- The description includes markdown formatting via a 3rd party package called 'Django Summernote'.
