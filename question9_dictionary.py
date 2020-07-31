string="MISSISSIPPI"
i=0
lis=[ ]
list2=[]
count=0
while i <len(string):
	j=0
	stn=" "
	while j<len(string):
		if string[i]==string[j]:
			stn=string[i]
			count=count+1
			lis.append(stn)
			lis.append(count)
		if string[i]not in lis[j]:
			list2.append(lis)
		j=j+1
	i=i+1
print (lis)
