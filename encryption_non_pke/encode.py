#For this portion of the homework, I've chosen to use a substitution cipher. This means each letter of the alphabet will be encoded with a different letter from the alphabet in a one-to-one mapping. The user that is attempting to decode the message will know the mappings of the original letters to the encoded letters, so they can work backwards to decode.

#Below is a commented example of how I could build this algorithm.

import random

def encode(message):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.?!1234567890"
  new_alphabet = ""

  #Randomly map the original alphabet onto a new alphabet
  for i in range(0,len(alphabet)-1):
    #Choose a random letter and add it into the new alphabet
    letter = alphabet[random.randint(0,len(alphabet)-1)]
    new_alphabet += letter
    #Remove the letter from the original alphabet
    alphabet = alphabet.replace(letter, "")

  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ ,.?!1234567890"
  encoded = ""
  for letter in message:
    #Replace each letter in the message with the corresponding letter from the new alphabet
    position = alphabet.index(letter)
    encoded += new_alphabet[position]
  
  print(new_alphabet)
  print(encoded)
  
encode("HELLO, I HAVE ENCODED A MESSAGE WITH BASIC PUNCTUATION!")
    