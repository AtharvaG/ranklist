import re 
from operator import itemgetter

file = open('/home/atharva/Downloads/result.txt', 'r')
roll = []
sgpa = []
reg = re.compile('S1500')
reg1 = re.compile('SGPA')
count = 10 
for line in file:
	
	count +=1  
	if(reg1.match(line)):
		count =0 

	if(count ==2):
		sgpa.append(line)
		count = 10 
			
	if(reg.match(line)):
		roll += [line]
		
file.close()

dictionary  = dict(zip(roll, sgpa))
sort_dict = sorted(dictionary.items(), key = itemgetter(1))
print (sort_dict)










