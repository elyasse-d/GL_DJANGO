# Library Management Project for GL (Software Engineering)
<div align="center">

![Main](./libra.png)

</div>

![Main](./main.png)

![Prev](./prev.png)

# Installation
this project requires Python3 , First
install Python Requirements
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

