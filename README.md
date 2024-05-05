# GL_DJANGO
First Pull the Project


Second , Use this command
```
pip install -r requirement.txt
```
Install NPM

Setup The Envirement 
```
python manage.py migrate
```

run the Dev Server 
```
python manage.py tailwind start 
python manage.py runserver
```
>To add image to your html , use {% load static %} and {% static 'biblio/ficher.png' %} 

The project Map
```
projct/
    ~/projct    #core
    ~/appbib    #tailwind app
        ~/static       #images, js...
        ~/static_src  #tailwind config
            ~/src
                ~/tailwindcss.js.config #tailwind configuration file
        ~/templates     #html
    ~/biblioapp #app  #for Bootstrap
        ~/static       #images, js...
        ~/templates     #html
    .manage.py
```
ALL PAGES ARE SETTED
