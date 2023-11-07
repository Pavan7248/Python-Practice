#Program to write the multiplication table of a number entered b y user
a = (input("Enter the number: "))
print(f"Multiplication table of {a} is given below:")
#Using Exception Handling 
try:
  for i in range(1,11):
    print(f"{int(a)} * {i} = {int(a)*i}")
except Exception:
  print("Please enter a valid number")

#Using finally keyword
finally:
  print("Thank you for using this program")
