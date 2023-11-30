# Oasis Froum
This Oasis Forum is used as a spiritual healing forum, by posting some heart-warming sentences to share everyone's current status, which can also help some people who are at a low point.



## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=Vue.vscode-typescript-vue-plugin).


## Oasis Startup Guide

* You can use `git clone git@github.com:david188888/Oasis.git` to clone the project which is in my [repositories](https://github.com/david188888?tab=repositories).<br>&emsp;

* Unzip the zip folder



### The mian requirements of the project
* Python &nbsp;3.10.0
* Node.js&nbsp;18.15.0
* npm&nbsp;9.6.2
* vite.js/plugin-vue&nbsp;4.3.4
* Django&nbsp;    4.1
* djangorestframework&nbsp;3.14.0

1. The requirements of the backend are in the [requirements.txt](./backend/requirements.txt).
2. The requirements of the frontend are in the [package.json](./frontend/Oasis/package.json).




### Start the frontend server of `Vue3`
 * You should install the `node` first.
 * go to the __Oasis__ folder.
 * use `npm install` to install the dependencies.
 * use `npm run dev` to start the frontend server of `Vue3`.



### Run the backend server of `Django`
* create a virtual environment and switch to backend folder.
* Install the django using `pip install django` first.
* Run the command `pip install -r requirements.txt` to install the dependencies.
* Go to the __backend__ folder.
* Migrate the database using `python manage.py makemigrations` firstly and then using `python manage.py migrate`.

* Using `python manage.py runserver` to start the backend server of `Django`.





