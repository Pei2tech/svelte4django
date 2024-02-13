import sys
import os
import time
from pathlib import Path
import hashlib

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent

buildmaxtime = 20 # sec


js_assets_head = " <script type=\"module\" href=\"{% static 'assets/"
js_assets_end = "' %}\"></script>\n"
assets_head={
    ".js":" <script type=\"module\" href=\"{% static 'assets/",
    ".css":" <link rel=\"stylesheet\" href=\"{% static 'assets/",
    ".ico":" <link rel=\"ico\" href=\"{% static 'assets/",
    ".svg":" <link rel=\"icon\" href=\"{% static 'assets/",
}
assets_end ={
    ".js": "' %}\"></script>\n",
    ".css": "' %}\">\n",
    ".ico": "' %}\">\n",
    ".svg": "' %}\">\n",
}

html_assets={
    "main.js":" <script type=\"module\" crossorigin src=\"{% static 'assets/",
}

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
       if not self.templateDir.exists():
           self.templateDir.mkdir(parents=True, exist_ok=True)
       if not self.staticDir.exists():
           self.staticDir.mkdir(parents=True, exist_ok=True)
       if not self.assetsDir.exists():
           self.assetsDir.mkdir(parents=True, exist_ok=True)


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

    def readindex(self):
        file= BASE_DIR / 'index.html'
        html = ""
        with open(file) as u1:
            for content in u1:
                if content.find("<!DOCTYPE html>") != -1 or content.find("<!doctype html>") != -1:
                    if content.find("<!DOCTYPE html>") != -1:
                        index = content.find("<!DOCTYPE html>") + len("<!DOCTYPE html>")
                    elif content.find("<!doctype html>") != -1 :
                        index = content.find("<!doctype html>") + len("<!doctype html>")
                    content = content[:index] + "\n {% load static %} \n" + content[index:]
                    html = html + content
                elif content.find("favicon.ico") != -1:
                    if os.path.exists(self.staticDir / "favicon.ico"):
                        r1 = content.replace(' href="', ' href="{% static \'')
                        r2 = r1.replace('.ico"', '.ico\' %}"')
                        html= html + r2
                elif content.find("main.js") !=-1:
                    continue
                else:
                    html = html + content
        self.html=html

    def checkdebugassets(self):
        self.readindex()
        if os.path.exists(self.assetsDir):
            with os.scandir(self.assetsDir) as items:
                for entry in items:
                     os.remove(entry.path)
        count=0
        while(True):
            html = ""
            with os.scandir(self.assetsDir) as items:
                assetf=[]
                for entry in items:
                    extension = (Path(entry.name).suffix)
                    assetf.append(entry.name)
                    if entry.name in html_assets.keys():
                        time.sleep(0.2)
                        html =html+html_assets[entry.name]+ entry.name +assets_end[extension]
                    else:
                        time.sleep(0.2)
                        html =html+ assets_head[extension] + entry.name + assets_end[extension]
                    if entry.name == "favicon.ico":
                        Path(entry.path).rename(Path(self.staticDir, entry.name))

                if html != "" and ("main.js" in assetf) :
                    if self.html.find("</head")!=-1:
                        index = self.html.find("</head>")
                        self.html = self.html[:index] + html + self.html[index:]
                        return True
                if count>buildmaxtime:
                    print("time out fail!!")
                    return False
            count +=1
            time.sleep(1)

    def checkbuildassets(self):
        self.readindex()
        html = ''
        vendorfile=[]
        vendortag=[]
        r1=""
        if os.path.exists(self.assetsDir):
            print("add hashed tag to main files")
            with os.scandir(self.assetsDir) as items:
                for entry in items:
                    if entry.is_file():
                        p = Path(entry.path)
                        suffix = p.suffix
                        hashtag = self.hashfile(entry.path)
                        if entry.name in ['main.js']: # , "main.css"]:
                             newName = p.rename(Path(p.parent, f"{p.stem}_{hashtag}{p.suffix}"))
                             mainName=newName
                        elif suffix in [".js", ".css"]:
                             newName = p.rename(Path(p.parent, f"{p.stem}_{hashtag}{p.suffix}"))
                             if suffix == ".js":
                                 vendorfile.append(entry.name)
                                 vendortag.append(newName)
                        if entry.name=="favicon.ico":
                            print(p.rename(Path(self.staticDir, entry.name)))
                            continue
                        elif suffix in [".js", ".css"]:
                            print(newName)
                        else:
                            print(p.absolute())

                        if entry.name in html_assets.keys():
                            html = html + html_assets[entry.name] + newName.name + assets_end[suffix]
                        elif suffix in [".js", ".css"]:
                            html = html + assets_head[suffix] + newName.name + assets_end[suffix]
                        else:
                            html = html + assets_head[suffix] + entry.name + assets_end[suffix]
                for index, name in enumerate(vendorfile):
                    content = mainName.read_text()
                    r1 = content.replace(name, vendortag[index].name)
                if r1!="":
                    mainName.write_text(r1)
                if html != "":
                    if self.html.find("</head") != -1:
                        index = self.html.find("</head>")
                        self.html = self.html[:index] + html + self.html[index:]
                        return True

    def writefile(self,file):
        file2= Path(self.dirname) / "templates" / file
        with open(file2,"w") as u2:
            u2.write(self.target)

    def removefile(self,file):
        if os.path.exists(file):
           os.remove(file)


    def hashfile(self,filename):
        with open(filename, "rb") as f:
            buf = f.read()
        m = hashlib.md5(buf)
        return m.hexdigest()[0:12]

    def main(self):
        if self.checkprojctName():
            self.assignDir()
        else:
            print("no Django project founded!")
            exit(0)
        if len(sys.argv) >= 2:
            if sys.argv[1]=="debug":
                if self.checkdebugassets():
                    with open(self.indexfile, "w") as file:
                        file.write(self.html)
                exit()
        if self.checkbuildassets():
            with open(self.indexfile, "w") as file:
                file.write(self.html)



if __name__ == '__main__':
    to_replace = ToReplace()
    to_replace.main()
