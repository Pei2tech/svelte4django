Introduction  
===========  
A simple template for Django + Svelte + Vite + Tailwindcss.     

Installation 
========
## install by git clone

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

## Install by command line 

install vite with svelte
```
$npm init @vitejs/app projectname 
# choose svelte, cd into directory 
$cd projectname
$npx svelte-add@latest postcss
$npx svelte-add@latest tailwindcss
```
Install the node dependencies 
```
$npm install 
```
In order to support postcss, add file app.postcss

```
$cd src
$touch app.postcss
```
add below content into app.postcss
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```
replace "./app.css" to "./app.postcss" in the main.js
```
import "./app.postcss";
import App from "./App.svelte";

const app = new App({
  target: document.getElementById("app"),
});

export default app;
```

Install django at the **root of your project**. It is the same as installation by git clone.  after that, you need create a project by the command "django-admin".   Below codes just use "mysite" as the django project, however you can change what you want.
```
$django-admin startproject mysite
```
you can use below command to check the installation of django is ok or not.

```
$cd mysite
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
ALLOWED_HOSTS = ['127.0.0.1','loclahost']

TEMPLATES = [
    {
       ...
        'DIRS': [BASE_DIR / 'templates'],
       ...
    },
]

```

If anything is done, please copy the mvindex,py and vite.config.js to the root of this project, and then modify the outDir of vit.config.js as the project name of django is not "mysite". 

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

##run on local debug mode  

You can debug frontend (svelte side) and backend (django side) at the same time , so you need  two terminals to run it.   

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
transforming (1) src/main.js
warn - You have enabled the JIT engine which is currently in preview.
warn - Preview features are not covered by semver, may introduce breaking changes, and can change at any time.
✓ 5 modules transformed.
mysite/statics/assets/main.js     1.79 KiB / gzip: 0.96 KiB
mysite/statics/assets/vendor.js   3.07 KiB / gzip: 1.42 KiB
mysite/statics/assets/main.css    5.72 KiB / gzip: 1.97 KiB
built in 898ms.
```   
 Just open your browser at  [http://127.0.0.1:8000](http://127.0.0.1:8000).  The "hello world!!" should be show on the screen.    

### run on production mode  

**svelte side**  

It will add hash on the asset files.  

```  
$npm run build
```  

You will see the files already hashed as the following ouput.    

```
add hashed tag to filename:
.../mysite/statics/assets/main_b915bd7db1c7.js
.../mysite/statics/assets/vendor_3e5f9a7a9227.js
.../mysite/statics/assets/favicon.ico
.../mysite/statics/assets/main_925825c51380.css
```

**django side**    
you may use gunicorn, nginx or other else to run django. It is out of the scope of this template.    
