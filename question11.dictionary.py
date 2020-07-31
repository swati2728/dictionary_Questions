my_dict = {
    'a':50, 
    'b':58, 
    'c':56,
    'd':40, 
    'e':100, 
    'f':20
    }
maxi=[]
for i in my_dict:
	print(my_dict[i])	
print(max(my_dict.values()))    

# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
# print(max(numbers))
# index=0
# while index<len(numbers):
# 	print(numbers[index])
# 	index=index+1
# print(max(numbers))	

num = [50,56,12,7,19]
a = 0
maxi = 0
while (a<len(num)):
	if (num[a] > maxi):
		maxi = num[a]
	a =  a + 1
print(maxi)