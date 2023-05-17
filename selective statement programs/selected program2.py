a=int(input("Enter the first side"))
b=int(input("Enter the second side"))
c=int(input("Enter the third side"))
if((a+b<c) and (b+c>a) and (a+c>b)):
    print("The triangle is possible")
else:
    print("The triangle is not possible")