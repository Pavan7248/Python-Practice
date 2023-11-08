import random
import string

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
def encode_word(word):
  if len(word) > 3:
    first_letter = word[0]
    word = word[1:] + first_letter
    random_chars = ''.join(random.choice(string.ascii_letters) for _ in range(3))
    encoded_word = random_chars + word + random_chars
  else:
    encoded_word = word[::-1]
  return encoded_word


def decode_word(word):
  if len(word)<3:
    decoded_word = word[::-1]
  else:
    word = word[3:-3]
    last_letter = word[-1]
    decoded_word = last_letter + word[:-1]
  return decoded_word

def encode_message(message):
  words = message.split()
  encoded_words = [encode_word(word) for word in words]
  encoded_message = ' '.join(encoded_words) 
  return encoded_message

def decode_message(mesage):
  words = message.split()
  decoded_words = [decode_word(word) for word in words]
  decoded_message = ' '.join(decoded_words) 
  return decoded_message

while True:
  choice = input("Do you want to code or decode \n Type c for encoding and d for decoding ").lower()
  if choice == 'c':
    message = input("Enter the message to encode: ")
    encoded_message = encode_message(message)
    print(f"The encoded message is: {encoded_message}")
  elif choice == 'd':
    message = input("Enter the message to decode: ")
    decoded_message = decode_message(message)
    print(f"The decoded message is: {decoded_message}")
  else:
    print("Invalid choice")

  another_message = input("Do you want to encode another message? y/n")
  if another_message != 'y':
    break
    



  
    
    