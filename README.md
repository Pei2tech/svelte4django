Introduction  
===========  
A simple template for Django + Svelte5 + Vite + Tailwindcss.   
It supports HMR for debug mode.  

**Note:**   
    1. If you are new to use restful api in the Django, you should try the [Django Ninja](https://django-ninja.rest-framework.com).    
    2. To use Svelte 5 and Django together, the recommended installation method is via the command line, as described below.     
    3. If you want to use router, you can also refer [Is there a router?](https://svelte.dev/docs/faq#is-there-a-router) or search from [github](https://github.com/search) for other choices.   
    4. If using git clone for installation, the client-side router [svelte5-route](https://github.com/jpcutshall/svelte5-router) and some sample code have been added to the template.     
    5. If you still wish to use Svelte 4, please refer to the [svelte4-vite-django](https://github.com/Pei2tech/svelte4-vite-django). 
    
   
Installation 
========
You can install it by git clone (router included) or command line(step by step).

## Install it by git clone (Svelte 5)

**Clone this repository and go into the directory**

```
$ git clone  https://github.com/Pei2tech/svelte4django.git projectname
$ cd projectname 
```

**Install Django**

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

## Install it by command line (Svelte 5)

Before installing it, please download **mvindex.py** from this repository. 

install vite with svelte
```
$npm create vite@latest projectname -- --template svelte
```
Go into the directory of projectname and then add tailwindcss for svelte
```  
$cd projectname
$npx sv add tailwindcss

```
Install the node dependencies 
```  
$npm install 
```

Install django at the **root of your project**. 

```   
$ pip install django   
```   

After that, you need create a project by the command "django-admin".   Below codes just use "mysite" as the django project, however you can change what you want.
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

If anything is done, please copy the mvindex,py from this repository to the root of your project, and then modify the vite.config.js as described below. Note:you may also modify the outDir as the project name of django is not "mysite". 

```
import tailwindcss from "@tailwindcss/vite";
import { defineConfig } from 'vite'
import { svelte } from '@sveltejs/vite-plugin-svelte'
import path from "path";
import { fileURLToPath } from 'url';
import { dirname } from 'path';

const _filename = fileURLToPath(import.meta.url);
const _dirname = dirname(_filename);

// https://vite.dev/config/
export default defineConfig({
  plugins: [svelte(), tailwindcss()],
  build: {
    // below for main.js
    outDir: path.join(_dirname, "mysite/statics/assets"),
    rollupOptions: {
      output: {
        entryFileNames: `[name].js`,
        chunkFileNames: `[name].js`,
        assetFileNames: `[name].[ext]`,
      },
      input: path.resolve(_dirname, "src", "main.js"),
      // external: [
      // ],
    },
  },
})

```

We use the del-cli dependence to clear the directory, so you may install it first. 

```
$npm i -D del-cli
```

Please modify the scripts of package.json as following.  Please also change the mysite as you use another project name for django. 

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

When running the project for the first time, please run the Svelte side first in order to properly initialize the target directory.

**Svelte side**    

Take the terminal on, and change into the project root to run below command.  

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

**Django side**  

Change into the root directory (mysite) of django, if you haven't already, and run the migrate. After that, you can run the development server up.    
Note: please make sure the virtual environment running if you have used it.   
```  
(.venv)...$cd mysite
(.venv)...$python manage.py migrate
...
(.venv)...$python manage.py runserver
```  
You will see the output on the command line for Starting development server at http://127.0.0.1:8000/ .  

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
  1. The file App.svelte, created by Vite, uses the "import" function to reference the "src" of the logo file, which does not work for Django. The solution is to assign a new variable for the logo file with a static path.  
