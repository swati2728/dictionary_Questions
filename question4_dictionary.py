# Dic= {
#         1: 'NAVGURUKUL',
#         2: 'IN',  
#   	    3:{    
#              'A' : 'WELCOME',
#              'B' : 'To',
#              'C' : 'DHARAMSALA'
#             }
#         }
# del(Dic[3]['A'])
# print(Dic)        

# a="*"
# i=1
# while i<=5:
# 	print((6-i)*a)
# 	i=i+1
#  

i=1
while i<=10:
	year=int(input("enter the year"))
	if year%4==0 and year%100!=0 or year%400==0:
		print(year,"leap year")
	else:
	    print(year,"normal year")
	i=i+1    	