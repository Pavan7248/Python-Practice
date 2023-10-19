#lists can be changed
list = [1, 2, 3, 4, "Pavan", "Navdeep" ]
print(list)
print(list[0])
print(type(list))
print(len(list))
print(list[-1])
print(list[-2])
print(list[-3])
if(4 in list):
  print("Yes")
else:
  print("No")

print(list[1:5:2])

#List comprehension
list = [x for x in range(10)]
print(list)
list = [x*x for x in range(10) if x%2==0]
print(list)
