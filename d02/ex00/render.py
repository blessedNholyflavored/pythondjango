#! /usr/bin/env python3
import sys
import re
import settings 

def main():
    if len(sys.argv) != 2:
        return print("wrong number of arguments")
    path = sys.argv[1]
    print(path)
    # f = open('myCV.template', 'r')
    # The re module offers a set of functions that allows us to search a string for a match:

    remod = re.compile(".*\.template")
    # if not remod == path:
    if not remod.match(path):
        return print("lol")
    print("jerentre")
    file = open(path, "r")
    # print(file.readline())
    # content=  "".join(line.strip() for line in file)  
    content=  "".join(file.readlines())  
    print(content)
    file.close()

    txt = content.format(nom=settings.nom, prenom=settings.prenom, age=settings.age, passion=settings.passion)
    remod = re.compile("(\.template)")
    path = "".join([path[0:remod.search(path).start()], ".html"])
    f = open(path, "w")
    f.write(txt)
    f.close()

    
    
    # exec(code)




if __name__ == '__main__':
    main()
