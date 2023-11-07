#Program to write the multiplication tab;le of a number entered b y user
a = int(input("Enter the number: "))
print(f"Multiplication table of {a} is given below:")
#Using Exception Handling 
try:
  for i in range(1,11):
    print(f"{a} x {i} = {a*i}")
except:
  print("Please enter a valid number")
