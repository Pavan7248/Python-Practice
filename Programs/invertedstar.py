#Write a program to print inverted star

n = int(input("Enter a number: "))

for i in range (n, 0, -1):
  print((n-i) * ' ' + i * '*')