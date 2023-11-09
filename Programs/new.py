def has_two_nineteen_and_at_least_three_five(lst):
  count_nineteen = lst.count(19)
  count_five = lst.count(5)

  return count_nineteen == 2 and count_five >= 3

# Input a list of integers from the user
item = 0
lst = []
input_str = input("Enter a list of integers separated by spaces: ")
input_list = input_str.split() 
# Split the input string by spaces
for item in input_list:
 
  item = int(item)
  lst.append(item)
result = has_two_nineteen_and_at_least_three_five(lst)
print("Does the list meet the criteria? ", result)
