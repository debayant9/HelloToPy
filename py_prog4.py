def findfact(arg):
    sum = 1
    if arg != 0:
        for i in range(1,arg+1):
            sum = sum *i
        print(sum)
    else:
        print("Please give a valid number")

n = input("Enter a number: ")
findfact(int(n))
