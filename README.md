Introduction  
===========  
A simple template for Django + Svelte + Vite + Tailwindcss.   
It supports HMR for debug mode.  

**Note:**   
    1. If you are new to use restful api in the Django, you should try the [Django Ninja](https://django-ninja.rest-framework.com).   
    2. If you want to use router, the [svelte-navigator](https://github.com/mefechoel/svelte-navigator) could be a good option.

   
Installation 
========
You can install it by git clone or command line(step by step).

## Install it by git clone

**Clone this repository and go into the directory**

```
$ git clone  https://github.com/Pei2tech/svelte4django.git projectname
$ cd projectname 
```

This template uses [poetry](https://python-poetry.org/ "poetry") to manage python packages. However, you can just install django by pip as you don't use poetry.    

```
poetry shell
poetry install
```  
or   
```   
$ pip install django   
```   

for security issue, please use below command to get security key and then update it in the setting.py.       
```  
$python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```  
   
After that, you need Install the node dependencies by npm or yarn.  
with npm   
```  
$npm install    
```  

## Install it by command line 

Before installing it, please download **mvindex.py** and **vite.config.js** from this repository. 

install vite with svelte
```
$npm init vite projectname
# choose svelte, cd into directory 
$cd projectname
$npx svelte-add@latest postcss
$npx svelte-add@latest tailwindcss
```
Install the node dependencies 
```
$npm install 
```

Install django at the **root of your project**. It is the same as installation by git clone.  after that, you need create a project by the command "django-admin".   Below codes just use "mysite" as the django project, however you can change what you want.
```
$django-admin startproject mysite
```
you can use below command to check the installation of django is ok or not.

```
$cd mysite
$python manage.py migrate
$python manage.py runserver
```

please update the urls.py to support index.html
```
from django.views.generic import TemplateView
urlpatterns = [
    path("",TemplateView.as_view(template_name="../templates/index.html")),
    path('admin/', admin.site.urls),
]
```

We use "templates" as the directory of html file, please update ALLOWED_HOSTS and the DIRS of TEMPLATES in the file named settings.py
```
ALLOWED_HOSTS = ['127.0.0.1','localhost']

TEMPLATES = [
    {
       ...
        'DIRS': [BASE_DIR / 'templates'],
       ...
    },
]

```

Please also add the static directory in the settings.py.
```
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

STATIC_ROOT = 'staticfiles'

```

If anything is done, please copy the mvindex,py and vite.config.js from this repository to the root of your project, and then modify the outDir of vit.config.js as the project name of django is not "mysite". 

```
outDir: path.join(_dirname, "mysite/statics/assets"),
```
Please modify the scripts of package.json as following.  We use the del-cli dependence to clear the directory, so you may install it first.  Please also change the mysite as you use another project name for django. 

```
"scripts": {
    "delete": "del --force mysite/statics/assets",
    "dev": "vite",
    "build": "npm run delete && vite build && npm run move",
    "move": "python mvindex.py",
    "serve": "vite preview",
    "watch": "python mvindex.py debug & vite build --watch "
  },

```

Running
======

## run on local debug mode  

In order to debug frontend (svelte side) and backend (django side) at the same time , you need open two terminals.   

**Django side**  

Change into the root directory (mysite) of django, if you haven't already, and run the migrate. After that, you can run the development server up.    
Note: please make sure the virtual environment running if you have used it.   
```  
(.venv)...$cd mysite
(.venv)...$python manage.py migrate
...
(.venv)...$python manage.py runserver
```  
You will see the ouput on the command line for Starting development server at http://127.0.0.1:8000/ .  

**Svelte side**    

Take another terminal on, and change into the project root to run below command.  

```  
$npm run watch
```  

You’ll see the following output on the command line:   

```
watching for file changes...

build started...
✓ 26 modules transformed.
mysite/statics/assets/main.css  7.39 kB │ gzip: 2.19 kB
mysite/statics/assets/main.js   5.22 kB │ gzip: 2.43 kB
built in 735ms.
```   
 Just open your browser at  [http://127.0.0.1:8000](http://127.0.0.1:8000).  The "hello world!!" should be show on the screen if the installation is made by git clone.     

## run on production mode  

**svelte side**  

It will add hash on the asset files.  

```  
$npm run build
```  

You will see the files already hashed as the following ouput.    

```
add hashed tag to main files:
.../mysite/statics/assets/main_b915bd7db1c7.js
.../mysite/statics/favicon.ico
.../mysite/statics/assets/main_925825c51380.css
```

**django side**    
you may use gunicorn, nginx or other else to run django. It is out of the scope of this template.    

## Note:
  1. Some packages still don't support svelte 4 yet, you can downgrade svelte to version 3.x.
  2. The file App.svelte, created by Vite, which uses "import" function to the "src" of the logo file can not work for django. The solution is to assign a new variable for the logo file of static path.
