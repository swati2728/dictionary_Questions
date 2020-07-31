# list1=[{1:2},{2:3},{5:6}]
# new_list=[]
# index=0
# while index<len(list1):
# 	for j in list1[index]:
# 		print(list1[index][j])
# 		new_list.append(list1[index][j])
# 	index=index+1
# print(new_list)		
# 	


# ======================================================

list1=[
    {"first":"1"}, 
    {"second": "2"}, 
    {"third": "1"}, 
    {"four": "5"}, 
    {"five":"5"}, 
    {"six":"9"},
    {"seven":"7"}
]
new_list=[]
index=0
while index<len(list1):
	for j in list1[index]:
		if list1[index][j]not in new_list:
			# print(list1[index][j])
			new_list.append(list1[index][j])
		index=index+1
print(new_list)		
	