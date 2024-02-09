#! /usr/bin/env python3

d = {
'Hendrix' : '1942',
'Allman' : '1946',
'King' : '1925',
'Clapton' : '1945',
'Johnson' : '1911',
'Berry' : '1926',
'Vaughan' : '1954',
'Cooder' : '1947',
'Page' : '1944',
'Richards' : '1943',
'Hammett' : '1962',
'Cobain' : '1967',
'Garcia' : '1942',
'Beck' : '1944',
'Santana' : '1947',
'Ramone' : '1948',
'White' : '1975',
'Frusciante': '1970',
'Thompson' : '1949',
'Burton' : '1939',
}

def mysort():
   list = sorted([(key, item) for key, item in d.items()],key=lambda list: (list[1], list[0])) 
   for i in list:
    print(i[0])
  

if __name__ == '__main__':
    mysort()


    # mylist = sorted(mylist, key=itemgetter('name', 'age'))
# mylist = sorted(mylist, key=lambda k: (k['name'].lower(), k['age']))
# mylist = sorted(mylist, key=lambda k: (k['name'].lower(), -k['age']))
    
# list = sorted([(key, item) for key, item in d.items()],
                #   key=lambda list: (list[1], list[0]))
    # [print(el[0]) for el in list]