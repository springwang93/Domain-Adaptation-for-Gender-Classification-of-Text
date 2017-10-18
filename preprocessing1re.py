
#remove non English word from text.


import re 
import nltk

f= open('C:/Users/WANGSITONG/Desktop/research/female.txt','r',encoding='utf-8')  
f1=open('C:/Users/WANGSITONG/Desktop/research/female1.txt','w')


for line in f:
    regex=re.compile('[^/a-zA-Z0-9 \t]') #\t tab
    result=regex.sub('',line)
    
    result = result.replace("\t", " ")
    f1.write(result+"\n") #\n space 
    print(result+"\n")

f1.close()
