"""
This is fun

"""

lis = [67,90,123]

#WITH usage
def convert(filename):
 with open(filename,'w') as fil:
  for i in lis:
   if i > -273:
    temp_f = i*9/5+32
    fil.write(str(temp_f) + "\n")
   else:
    print("Not appr temperature")
	
    


def add(n1,n2):
    res = n1 + n2
    print("Result")
    return res

#print(convert(-273.15))

if add(190,45) > -273:
	print("Wrong values")
elif add(190,45) == 235:
	print("Exact values")
else:
	print("Wrong values")

a = 60
if a == 60 and a == 80:
   print("Got it")

convert("lop2")







