import sys 
try:
   x = int(input("input1= "))
   y = int(input("input2= ")) 
except ValueError:
    print("error:invalid value entered ")
    sys.exit(1)

try:  
    result = x/y 
except ZeroDivisionError:
    print("error: divided by zero ")
    sys.exit(1)

    print(f"{x}/{y} = {result} ")