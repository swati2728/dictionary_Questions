dic={
    "ball":"red",
    "bat":4,
    "wicket":8,
    "ball":"green",
    "bat":3
    }
# print ("Original list : " + str(dic)) 
new_dic={}
# second_dic={}
for i in dic:
	if (dic[i]not in new_dic):
		new_dic.update(dic)
# 		for j in dic:
# 			if dic[i]==new_dic[j]:
# 				second_dic.update(new_dic)
print(new_dic)
# print(second_dic)




