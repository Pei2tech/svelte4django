Introduction  
===========  
A simple template for Django + Svelte + Vite + Tailwindcss.     

Installation  
========   
**Clone this repository and go into the directory** 

```
$ git clone  https://github.com/Pei2tech/svelte4django.git projectname
$ cd projectname 
```
This template uses [poetry](https://python-poetry.org/ "poetry") to manage python packages, but there is only django need to be installed. So, you can also install django by pip.    

```
poetry shell
poetry install
```  
or   
```   
$ python -m venv .venv  
$source ./.venv/bin/activate  
(.venv)...$ pip install django   
```
After that, you need Install the node dependencies by npm or yarn.  
with npm   
```  
$npm install    
```  

### run on local debug mode  

You can debug frontend (svelte side) and backend (django side) at the same time , so you need  two terminals to run it.   

**Django side**  

Change into the root of django directory (my site), if you haven't already, and run the migrate at the first time if you dn't want to ignore the warning. After that, you can run the development server up.    
Note: please make sure the virtual environment is running.   
```  
(.venv)...$cd mysite
(.venv)...$python manage.py migrate
...
(.venv)...$python manage.py runserver
```  
You will see the ouput on the command line for Starting development server at http://127.0.0.1:8000/ .  

**Svelte side**    

Take another terminal on, and change into the root directory of this project to run below command.  

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

It will add hash on asset files.  

```  
$npm run build
```  

