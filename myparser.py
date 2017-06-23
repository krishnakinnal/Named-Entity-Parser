from __future__ import print_function
from nltk.tag import pos_tag
from google import search
print ("\n\n\tEnter a string - ",end='')
string=raw_input()
words=string.split()
tokens=pos_tag(string.split())
propernouns=[word for word,pos in tokens if pos=='NNP']
n=len(propernouns)
if n==0:
    print ("\n\tNo proper nouns found :(\n\n")
    exit(0)
for i in range(n):
   itemno=1
   print ("\n\n\tThe search results for [[["+str(propernouns[i])+"]]] are...")
   for url in search(propernouns[i],stop=1):
        print ("\t"+str(itemno)+". "+url)
        itemno+=1
print ("\n\n")
