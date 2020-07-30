# 1 question

# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}
# i=0
# new_dic={}
# while i<len(dic1):
# 	new_dic.update(dic1)
# 	new_dic.update(dic2)
# 	new_dic.update(dic3)
# 	i=i+1
# print(new_dic)	

# question 2

# dict1={"name":"raju","marks":56}
# i=0
# while i <len(dict1):
# 	if "name" or "marks" in dict1:
# 		print("exist")

# 	else:
# 		print("not exist")
# 	i=i+1

# question 3

my_dict = {
        'data1':100,
        'data2':-54,
        'data3':247
       } 

sum = 0
for i in my_dict.values():
    sum=sum+i
print(sum)
# print(sum(my_dict.values()))

