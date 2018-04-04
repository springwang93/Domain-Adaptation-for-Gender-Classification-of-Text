import codecs
#0.delete duplicated rowC:\Users\WANGSITONG\Desktop\research_data\male
f_duplicate=open('C:/Users/WANGSITONG/Desktop/test/test327.txt','r',encoding='utf-8')

f_no_duplicate=open('C:/Users/WANGSITONG/Desktop/test/test000.txt','w',encoding='utf-8')

s=set()

for i in f_duplicate:
    s.add(i)

for i in s:
    f_no_duplicate.write(i)
f_no_duplicate.close()

#1.replace '{male,}','')
f_replace_start=codecs.open('C:/Users/WANGSITONG/Desktop/test/test000.txt','r+',encoding='utf-8')
lines=f_replace_start.readlines()

f_replace_start.seek(0,0)
for line in lines:
    new_line = line.replace('{male,}','')    
    f_replace_start.write(new_line)
   
    
f_replace_start.close()


#2.delete empty row
file_empty_row =open('C:/Users/WANGSITONG/Desktop/test/test000.txt','r+',encoding='utf-8')

lines=file_empty_row.readlines()
file_empty_row.seek(0,0)
for idx,line in enumerate(lines):
    if line.split():
        #print(idx,line)
        file_empty_row.write(line.replace('male,','male\t') )#3.comma is converted into tab 
        
file_empty_row.close()
