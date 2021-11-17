import sys
import os
import time
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

hostDir=Path("mysite")
templateDir = BASE_DIR / hostDir / "templates"
staticDir = BASE_DIR / hostDir / "statics"
assetsDir = staticDir / "assets"
indexfile = BASE_DIR / hostDir / "templates" / "index.html"
buildmaxtime = 10 # sec
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
  <title>{% block title %}{% endblock %} </title>
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


    def checkVendorcss(self):
        if os.path.exists(assetsDir):
            for entry in buildedfiles:
                if os.path.exists(assetsDir / entry):
                     os.remove(assetsDir / entry)
            count=0
            while(True):
                with os.scandir(assetsDir) as items:
                    for entry in items:
                        if entry.name in buildedfiles:
                            time.sleep(0.2)
                            if entry.name == "vendor.css":
                                return True
                            else:
                                return False
                    if count>buildmaxtime:
                        print("over time fail!!")
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
        sys.argv
        if len(sys.argv) < 2:
            self.dirname=Path(hostDir)
        else:
            if sys.argv[1]=="debug":
                self.html = html_head
                if self.checkVendorcss():
                    self.html += html_vendorcss
                self.html += html_tail
                with open(indexfile, "w") as file:
                    file.write(self.html)
                exit()
            self.dirname = sys.argv[1]
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
