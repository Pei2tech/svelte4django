import sys
import os
import time
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

buildmaxtime = 20 # sec
buildedfiles=["main.js","main.css","vendor.js", "vendor.css"]


html_head = """ 
<!DOCTYPE html>
 {% load static %}
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta HTTP-EQUIV="CACHE-CONTROL" CONTENT="NO-CACHE">
  <meta HTTP-EQUIV="EXPIRES" CONTENT="Mon, 20 Oct 2000 00:00:01 GMT">
  <title></title>
  <meta name=“description” content=“”>
  <script type="module" crossorigin src="{% static 'assets/main.js' %}"></script>
  <link rel="modulepreload" href="{% static 'assets/vendor.js' %}">
  <link rel="stylesheet" href="{% static 'assets/main.css' %}">
 """
html_vendorcss ="""
  <link rel="stylesheet" href="{% static 'assets/vendor.css' %}">
"""
html_tail = """
</head>
<body>
   <div id="app"></div>
  </body>
</html>
"""


class ToReplace(object):
    def __init__(self):
       self.dirname=""
       self.target=""
       self.html=""

    def assignDir(self):
       self.templateDir = BASE_DIR / self.dirname / "templates"
       self.staticDir = BASE_DIR / self.dirname / "statics"
       self.assetsDir = self.staticDir / "assets"
       self.indexfile = BASE_DIR / self.dirname / "templates" / "index.html"


    def checkprojctName(self):
        with os.scandir(BASE_DIR) as items:
            for entry in items:
                if entry.is_dir():
                    with os.scandir(entry.path) as subitems:
                        for subentry in subitems:
                            if subentry.is_file() and subentry.name=="manage.py":
                                self.dirname = Path(entry.name)
                                return True
        return False

    def checkVendorcss(self):
        if os.path.exists(self.assetsDir):
            for entry in buildedfiles:
                if os.path.exists(self.assetsDir / entry):
                     os.remove(self.assetsDir / entry)
        count=0
        while(True):
            with os.scandir(self.assetsDir) as items:
                for entry in items:
                    if entry.name in buildedfiles:
                        time.sleep(0.2)
                        if entry.name == "vendor.css":
                            return True
                        else:
                            return False
                if count>buildmaxtime:
                    print("time out fail!!")
                    return False
            count +=1
            time.sleep(1)
        return False

    def handlefile(self, file):
        with open(file) as u1:
            content=u1.read()
            if content.find("{% load static %}")==-1:
                index=content.find("<!DOCTYPE html>")+len("<!DOCTYPE html>")
                content = content[:index] + "\n {% load static %} \n" + content[index:]
            r1 = content.replace(' src="', ' src="{% static \'')
            r2 = r1.replace('.js"', '.js\' %}"')
            r3 = r2.replace(' href="', ' href="{% static \'')
            r4 = r3.replace('.css"', '.css\' %}"')
            r5 = r4.replace('.ico"', '.ico\' %}"')
            self.target=r5

    def writefile(self,file):
        file2= Path(self.dirname) / "templates" / file
        with open(file2,"w") as u2:
            u2.write(self.target)

    def removefile(self,file):
        if os.path.exists(file):
           os.remove(file)

    def main(self):
        if self.checkprojctName():
            self.assignDir()
        else:
            print("no Django project founded!")
            exit(0)
        sys.argv
        if len(sys.argv) >= 2:
            if sys.argv[1]=="debug":
                self.html = html_head
                if self.checkVendorcss():
                    self.html += html_vendorcss
                self.html += html_tail
                with open(self.indexfile, "w") as file:
                    file.write(self.html)
                exit()
            # self.dirname = sys.argv[1]

        if os.path.exists(Path(self.dirname) / "statics"):
            with os.scandir(Path(self.dirname) / "statics") as it:
                for entry in it:
                    if entry.name.endswith(".html") and entry.is_file():
                        self.handlefile(entry.path)
                        self.writefile(entry.name)
                        self.removefile(entry.path)
            exit()
        else:
            print("No dir list")
            exit()


if __name__ == '__main__':
    to_replace = ToReplace()
    to_replace.main()
