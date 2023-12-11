def replace_odd_with_minus_one(arr):
  return [-1 if num % 2 != 0 else num for num in arr]

# Example array
given_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Replacing odd numbers with -1
result_array = replace_odd_with_minus_one(given_array)
print(result_array)
