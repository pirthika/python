salary=int(input("Enter the salary"))
year=int(input("Enter the year"))
if(year>10):
    print("The bonus is",salary+salary*(10/100))
elif(year>6):
    print("The bonus is",salary+salary*(8/100))
else:
    print("The bonus is", salary+salary*(5/100))