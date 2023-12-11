# replace all odd numbers with -1

def replace_odd_with_minus_one(list):
  return [-1 if num % 2 != 0 else num for num in list]

# Example array
given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Replacing odd numbers with -1
result_list = replace_odd_with_minus_one(given_list)
print(result_list)
