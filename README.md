# GL_DJANGO
First Pull the Project


Second , Use this command
```
pip install -r requirement.txt
```
Setup The Envirement 
```
python manage.py migrate
```

run the Server 
```
python manage.py runserver
```
>To add image to your html , use {% load static %} and {% static 'biblio/ficher.png' %} 

The project Map
```
projct/
    ~/projct    #core
    ~/biblioapp #app
        ~/static       #images, js...
        ~/templates     #html
    .manage.py
```