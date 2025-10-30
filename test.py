#question 1
for x in range(4):
	print("*" * 9)   
  #2
print("***********")
print("*         *")
print("*         *")
print("***********")
#q3
for x in range(4):
    print("*" *x )
  #q4
  num = 512 
num2 =282
num4 = 47.48
num5 = 5
tol = num-num2
to = num4 + 5
total = tol/to
print (total)
#q5
import math 

num = int(input("Enter a number: "))
kill = pow(num,2)
print(f"the square of {num} is {kill}")
#q6
num = int(input("Enter number"))
for x in range(num,10):
    print(x  ,x*2 ,x*3 ,x*4,end= "--")
  #q7
weight = float(input("Enter the pounds to be converted to killograms"))
total = weight * 2.2
print(f"your killograms is {total:02}")
#q8
num = float(input("Enter the fist number: " ))
num2 = float(input("Enter the second number: "))
num3 = float(input("enter the third number: "))

totall = num + num2 + num3
avarage = totall/3
print(f"the total of the sum is {totall} and the avarage is {avarage}")
  
