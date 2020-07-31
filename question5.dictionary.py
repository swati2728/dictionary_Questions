# user_keys=["one","two","three","four","five"]
# user_values=[1,2,3,4,5,] 
# dic={}
# for key in user_keys:
# 	for value in user_values:
# 		# print(value)
# 		dic[key]=value
# 		user_values.remove(value)
# 		break
# print(str(dic))
# # print(user_values)




student_name=["yousuf","swati","sonu","sourab"]
student_marks=[42,5,36,25]
dic={}
for i in student_name:
	for j in student_marks:
		dic[i]=j
		student_marks.remove(j)
		break
print(str(dic))		