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


i=0

while i<n:
   itemno=1
#   print (propernouns[i+1],words.index(propernouns[i+1]),propernouns[i], words.index(propernouns[i])+1)
   try:
      if words.index(propernouns[i+1])==words.index(propernouns[i])+1:
         searchstring=str(propernouns[i])+" "+str(propernouns[i+1])
         i+=2
      else:
         searchstring=str(propernouns[i])
         i+=1
   except:
      searchstring=propernouns[i]
      i+=1
   print ("\n\n\tThe search results for [[["+str(searchstring)+"]]] are...")
   for url in search(searchstring,stop=1):
        print ("\t"+str(itemno)+". "+url)
        itemno+=1

print ("\n\n")
