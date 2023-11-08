#Handling errors
a = int(input("Enter any value between 10 and 20"))
#checking if the value is present between given numbers or not
if a < 10 or a > 20:
    raise ValueError(f"The value {a} is not between 10 and 20")

#raising a error if user enters a string other than quit
class CustomError(Exception):
  "Raised when the input value is string other than quit"
  pass

b = int(input("Enter any number between 20 and 30"))
if b < 20 or b > 30:
    raise CustomError(f"The value {b} is not between 20 and 30")