#Q1
import random
num = 3,4,5,6

random_num = random.choice(num)

print(random_num)

#Q2
import random

num1 = [x for x in range(1,50+1)]
num2  = [x for x in range(2,5+1)]
ran_num = random.choice(num1)  ** random.choice(num2)
print(ran_num)

#Q3
import random 

name = "allan"

num = random.randint(1,10)
print(f"Your random num is {num}")

for x in range(num):
    print(name)

#Q4
import random

num = random.uniform(1,10)

print(f"Your num is {num:.2f}")

#Q5
import random

num_1 = 1,2
num_2 = 1,2,3,4
final = [[x,y,z] for x in num_1 
         for y in num_2 
         for z in range(1,51+1)]
print(random.choice(final))

#Q6
x = int(input("Enter fist num: "))
y = int(input("Enter second num: "))
subtraction = x - y
sum = x + y
total = subtraction/sum
print(total)

#Q7
number = int(input("Enter number btwn -180-180: "))
if number % 1 == 0 or number % 360 == 0:
    print("Equivalent")
else:
    print("not equivalent")

#Q9
time = int(input("Enter hours btwn 1-12: "))
hours = int(input("How many hours ahead: "))
new = time + hours
times = new % 12

print(f"new hour {times} o'clock")
