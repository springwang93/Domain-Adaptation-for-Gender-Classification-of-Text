import re 
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
stemmer = SnowballStemmer("english")



f0= open('C:/Users/WANGSITONG/Desktop/research/male.txt','r',encoding='ISO-8859-1')  
f3=open('C:/Users/WANGSITONG/Desktop/research/male_p.txt','w',encoding='utf-8')
lines = []
buffer = ""

for line in f0:
    line = line.replace("\t", " ")
    words = line.split()
    if len(words) > 0:
        if words[0] == "male":
            lines.append(buffer)
            buffer = line
        else:
            buffer= buffer + line
lines.append(buffer)

for line in lines:
    #print(line.replace("\n"," "))
    f3.write(line.replace("\n"," ") + "\n")
    
f3.close()
        

f= open('C:/Users/WANGSITONG/Desktop/research/male_p.txt','r',encoding='utf-8')  
f1=open('C:/Users/WANGSITONG/Desktop/research/male1.txt','w',encoding='utf-8')
#f2=open('C:/Users/WANGSITONG/Desktop/research/male2.txt','w',encoding='utf-8')

for line in f:
    result= re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "httplink", line)
    regex=re.compile('[^/a-zA-Z0-9 \t]')
    result=regex.sub('',result)
    
    result = result.replace("\t", " ")
    
    words = word_tokenize(result)
    new_array = []
    for i in range(len(words)):
        newword = stemmer.stem(words[i])
        new_array.append(newword)
    if len(words) != 0:
        new_array.append(words[0])
    for i in range(1,len(words)-1):
        new_array.append(words[i]+"-"+words[i+1])
            #new_array.append(stemmer.stem(words[i])+" "+stemmer.stem(words[i+1]))

    #print(new_array)
    f1.write(" ".join(new_array)+"\n")
    #f2.write(" ".join(new_array2)+"\n")
    #print(" ".join(new_array)+"\n")

f1.close()
