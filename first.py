import re 
from operator import itemgetter
# import pdb

file = open('/home/atharva/Downloads/result.txt', 'r')
roll = []
sgpa = []
reg = re.compile('S1500')
reg1 = re.compile('SGPA')
count = 10 

dic ={};
dic1 = {};

rol=0;
for line in file:
	
	if(reg1.match(line)):
		line=file.next();
		line=file.next();
		dic[rol]=line;
		# pdb.set_trace()
			
	if(reg.match(line)):
		# pdb.set_trace()
		rol=line;
		# pdb.set_trace()
		dic[rol]=0;
		line = file.next()
		line = file.next()
		# pdb.set_trace()
		dic1[rol] = line;
		
file.close()

sort_dict=sorted(dic.items(),key=itemgetter(1),reverse=True)
sort_dict1 = sorted(dic1.items(), key= itemgetter(1))

infile = open ('out.txt', 'w')
for i in range(len(sort_dict)):
	for j in range(len(sort_dict1)):
		if (sort_dict[i][0] == sort_dict1[j][0]):
			print >> infile , i+1, "\n", sort_dict[i][0], sort_dict1[j][1] , sort_dict[i][1]

infile.close()





