print(" Program that accepts an integer (n) and computes the value of n+nn+nnn")
a = int(input("Enter a number:"))
n = str(a)
n1 = n + n
n2 = n1 + n
n3 = a + int(n1) + int(n2)

print("The sum of the number is:", n3)