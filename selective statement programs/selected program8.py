name=str(input("Enter the name:"))
age=int(input("Enter the age:"))
gender=str(input("Enter the gender:"))
g=gender.upper()
days=int(input("Enter the no of days:"))
if(age>=18 and age<30 and g=="m"):
    print(days*700)
elif(age>=18 and age<36 and g=="f"):
    print(days*750)
elif(age>=30 and age>=40 and g=="m"):
    print(days*800)
else:
    print(days*800)