student_name=["yousuf","swati","sonu","sourab"]
student_marks=[42,5,36,25]
dic={}
for i in student_name:
	for j in student_marks:
		dic[i]=j
		student_marks.remove(j)
		break
print(str(dic))		