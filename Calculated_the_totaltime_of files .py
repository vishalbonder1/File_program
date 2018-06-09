import os
import re
p=[]
reg=re.compile(r'((\d)|(\d\d)) min')
for folderName, subfolders, filenames in os.walk('T:\\andrioangi'):
    #print('The current folder is ' + folderName)
    for subfolder in subfolders:
        f=0
		
    for filename in filenames:
        h=1
        mo=reg.search(filename)
        if mo==None:
            continue
        else:   
            p.append(mo.group())		
		
		
    #print('')

#print(p)

#print(len(p))

l=[]
reg1=re.compile(r'(\d)|(\d\d)')

for i in p:
    mo1=reg1.search(str(i))
    if mo1==None:
            continue
    else:   
        l.append(mo1.group())	


#print(l)	 


sum=0
for j in l:	
    sum=sum+int(j)
    
sum=sum/2	
print(sum)	
	
	
	
	
	
	
	
	