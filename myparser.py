from __future__ import print_function
from nltk.tag import pos_tag
from google import search
print ("\n\n\tEnter a string - ",end='')
string=raw_input()
tokens=pos_tag(string.split())
#tokens=string.split()
print (tokens)
for token in tokens:
    print ("\n\n\tFor [["+token+"]] the search results are..")
    itemno=1    
    propernouns=[word for word,pos in tokens if pos=='NNP']
    for url in search(propernouns,stop=1):
    #for url in search(token,stop=1):
        print ("\t"+str(itemno)+". "+url)
        itemno+=1
