import urllib
import requests
from bs4 import BeautifulSoup
r = requests.get('http://google.com/').text
samplesoup = BeautifulSoup(r,'html.parser')
print samplesoup.prettify()


q = '''


x = urllib.urlopen(raw_input("Enter Website Here: "))



def acummulus(stringarry): #inputs an array split by href, outputs links
    accum = []
    for items in stringarry:
        i = 1
        ts = ""
        while i < len(items) and items[i] != "\"" and items[i] != "'": #we don't know which one could get thrown at us
            ts += items[i]
            i+=1
        accum += [ts]
    return accum

print acummulus((x.read()).split("href=")[1:]) #this way every link will be mentioned with this (we dropped the beginning as its garbage)

x.close()
'''
