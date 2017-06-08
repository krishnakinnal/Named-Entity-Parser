from __future__ import print_function
from nltk.tag import pos_tag
from google import search
print ("\n\n\tEnter a string - ",end='')
string=raw_input()
tokens=pos_tag(string.split())
propernouns=[word for word,pos in tokens if pos=='NNP']
for propernoun in propernouns:
   itemno=1
   print ("\n\n\tThe search results for [[["+str(propernoun)+"]]] are...")
   for url in search(propernoun,stop=1):
        print ("\t"+str(itemno)+". "+url)
        itemno+=1
print ("\n\n")
