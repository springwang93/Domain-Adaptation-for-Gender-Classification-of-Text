import re
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None



def lemmatize_sentence(sentence):
    res = []
    lemmatizer = WordNetLemmatizer()
    for word, pos in pos_tag(word_tokenize(sentence)):
        wordnet_pos = get_wordnet_pos(pos) or wordnet.NOUN
        res.append(lemmatizer.lemmatize(word, pos=wordnet_pos))

    return res



f= open('C:/Users/WANGSITONG/Desktop/test/test000.txt','r',encoding='utf-8') 
f1=open('C:/Users/WANGSITONG/Desktop/test/testformat0.txt','w',encoding='utf-8')

for line in f:
    result= re.sub("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "urllink", line)
    result=result.replace('male,','male\t')
    result=result.replace("," ," ")
    result=result.replace("."," ")
    result=result.replace("-"," ")
    result=result.replace("'m"," am")
    result=result.replace("'s"," is")
    result=result.replace("'re"," are")
    result=result.replace("'ve"," have")
    result=result.replace("'ll"," will")
    result=result.replace("'t"," not")
    result=result.replace("'d"," have")
    
    
    regex=re.compile('[^/a-zA-Z0-9 \t]')#去掉非英文但留下tab
    result=regex.sub('',result)#str
 
    words = word_tokenize(result)
    
    new_array = []
    
    if len(words) != 0:
        new_array.append(words[0]+'\t')
    for i in range(1,len(words)):
        
        stops = set(stopwords.words('english'))
        word_list = lemmatize_sentence(str.lower(words[i]))#newword is list words[i]is str
        filtered_words = [w for w in word_list if not w in stopwords.words('english')]#list
        newword=list(set(filtered_words))
    
        new_array.extend(newword)

    
            
    if len(words) != 0:
        new_array.append ('')
    
    for i in range(1,len(words)-1):
        new_array.append(words[i]+"-"+words[i+1])#words[i]+"-"+words[i+1]+":1" is str
      
        
   

    #print(new_array)
    
    f1.write(" ".join(new_array)+":1"+"\n") #new_array is list
    
    
f1.close()
f.close()

f2=open('C:/Users/WANGSITONG/Desktop/test/testformat0.txt','r+',encoding='utf-8')
lines=f2.readlines()

f2.seek(0,0)
   
for line in lines: 
    new_line=line.replace(' ',':1 ')
    new_line = new_line.replace('male\t:1 ','male\t')
    new_line= new_line.replace(' :1 ',' ')
    
    f2.write(new_line)
f2.close()

f3=open('C:/Users/WANGSITONG/Desktop/test/testformat0.txt','r+',encoding='utf-8')
lines=f3.readlines()

f3.seek(0,0)
   
for line in lines:
    new_line = line.replace(' :1','')
    f3.write(new_line)
f3.close()
  

'''
nltk stopword list
i
me
my
myself
we
our
ours
ourselves
you
your
yours
yourself
yourselves
he
him
his
himself
she
her
hers
herself
it
its
itself
they
them
their
theirs
themselves
what
which
who
whom
this
that
these
those
am
is
are
was
were
be
been
being
have
has
had
having
do
does
did
doing
a
an
the
and
but
if
or
because
as
until
while
of
at
by
for
with
about
against
between
into
through
during
before
after
above
below
to
from
up
down
in
out
on
off
over
under
again
further
then
once
here
there
when
where
why
how
all
any
both
each
few
more
most
other
some
such
no
nor
not
only
own
same
so
than
too
very
s
t
can
will
just
don
should
now
'''
