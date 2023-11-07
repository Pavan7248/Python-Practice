number = (input("Enter a list separated with white space:- "))
numbers = number.split()

even_num = []

for num in numbers:
  try:
    if int(num) % 2 == 0:
      even_num.append(num)
  except:
    pass

print("The even numbers are:- ", even_num)