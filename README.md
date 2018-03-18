# Archi :

## To launch :

+ Install dependencies :

  `pip install -r requirements.txt`

+ Make the migrations :

  `./manage.py makemigrations`

+ Migrate (create or update db) :

  `./manage.py migrate`

+ Collect staticfiles :

  `./manage.py collectstatic`

+ If you didn't already create one yet :

  `./manage.py createsuperuser`

+ Run the dev server :

  `./manage.py runserver`

+ Then try to reach `localhost:8000`

## Front developpement.

### Templates :

+ archi/templates/base.html

  Base template

+ archi/mygallery/templates/

  Templates for mygallery app.

### Static assets (JS, CSS, images) :

+ Assets should be put either in archi/static (related to the project) or in archi/mygallery/static/mygallery/ (related to the app mygallery) :


