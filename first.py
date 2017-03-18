import re 
from operator import itemgetter

file = open('/home/atharva/Downloads/result.txt', 'r')
roll = []
sgpa = []
reg = re.compile('S1500')
reg1 = re.compile('SGPA')
count = 10 

dic ={};
rol=0;
for line in file:
	
	if(reg1.match(line)):
		line=file.next();
		line=file.next();
		dic[rol]=line;
			
	if(reg.match(line)):
		rol=line;
		dic[rol]=0;
		
file.close()

sort_dict=sorted(dic.items(),key=itemgetter(1))
print (sort_dict)





