#Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
number = (input("Enter a list separated with white space:- "))
numbers = number.split()

  
a = 0
b = 0
  
for num in numbers:
  n = int(num)
  if n == 19:
    a += 1
  elif n == 5:
    b += 1
  

if a == 2 and b > 3:
  print("True")
else:
  print("False")
  
