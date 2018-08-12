
def thui(filename, stri):
 le = len(stri)
 gh = open(filename, 'r+')
 gh.write(stri)
 gh.seek(0)
 print(gh.read())
 gh.close()
 return le

def fileoperation(flename):
 fil = open(flename, 'r+')
 lis = [1,2,3]
 for i in lis:
  fil.write(str(i) + "\n")
 fil.seek(0)
 print(fil.read())
 fil.close()



filen = input("Please enter the filename: ")
val = thui(filen, "Kolkata")
print("Total variables written : ", val)
val = thui(filen, "Pune")
print("Total variables written : ", val)
val = thui(filen, "Bangalore")
print("Total variables written : ", val)


ref = input("please enter the 2nd filename: ")
fileoperation(ref)






