
#Task 1

#################################Answer 2:

ouput=[]
for x in range(2000,3200):
    if(x%7==0) and (x%5 != 0):
        ouput.append(str(x))
print(','.join(ouput))

#################################Answer 3:

fname = input("Enter your First Name")
lname= input("Enter your Last Name")
print("Hello "+lname[::-1]+" "+fname[::-1])

#################################Answer 4:

pi =22/7
diameter= 12
radius = diameter/2
volumne = (4/3)*pi*radius**3
print("Volume of the sphere is ", volumne)

#################################Task 2
#################################Answer 1:

data = input("Enter the values")
l= data.split(",")
print("List is : ",l)

################################Answer 2:

num= int(input("Enter the number of rows :"))
for i in range(num):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(num,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

#################################Answer 3:

word= input("Input word :")
print(word[::-1])

#################################Answer 4:

print("WE, THE PEOPLE OF INDIA,\n\t  having solemnly resolved to constitute India into a SOVEREIGN, ! \n\t\t\t SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \n\t\t\t and to secure to all its citizens")






