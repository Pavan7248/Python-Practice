# Write a Python program that accepts an integer and determines whether it is greater than 4^4 and which is 4 mod 34.


def mode(x):
  return (x > (4**4) and (x % 34) == 4)

x = int(input("Enter a number"))

print(mode(x))
