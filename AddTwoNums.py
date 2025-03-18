#Version1
#Add Two Numbers in Python
#Author: Shijia He
#Using the + Operator
a = 15
b = 12
#Adding two numbers
res = a + b
print(res)


#Version2
#Add Two Numbers in Python
#Author: Shijia He
#Using user input

#taking user input
a = input("First number: ")
b = input("Second number: ")

#converting inpt to float and adding
res = float(a) + float(b)
print(res)

#Version3
#Add Two Numbers in Python
#Author: Shijia He
#Using a function

#function to add two numbers
def add(a,b):
#converting input to float and adding
    result = float(a) + float(b)
    return result

#taking user input
a = input("First NUmber: ")
b = input("Second Number: ")

#calling function
res = add(a,b)
print("The Answer is")
print(res)

