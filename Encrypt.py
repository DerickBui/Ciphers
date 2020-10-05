# import random library to be able to use random functions
import random

# a normal alphabet
alphabets = "abcdefghijklmnopqrstuvwxyz"
# random key is generated
key = ''.join(random.sample(alphabets,len(alphabets)))

message1 = "He who fights with monsters should look to it that he himself does not become a monster . And if you gaze long into an abyss , the abyss also gazes into you ."

message2 = "There is a theory which states that if ever anybody discovers exactly what the Universe is for and why it is here , it will instantly disappear and be replaced by something even more bizarre and inexplicable . There is another theory which states that this has already happened ."

message3 = "Whenever I find myself growing grim about the mouth ; whenever it is a damp , drizzly November in my soul ; whenever I find myself involuntarily pausing before coffin warehouses , and bringing up the rear of every funeral I meet ; and especially whenever my hypos get such an upper hand of me , that it requires a strong moral principle to prevent me from deliberately stepping into the street , and methodically knocking people ’ s hats off - then , I account it high time to get to sea as soon as I can ."

# this a function that will encrypt the message
def encrypt(message, key):
  cipher = ""
  for i in message:
    if (i in key):
      cipher += key[alphabets.index(i)]
    elif (i.isupper()): # if uppercase letter is there
      cipher += key[alphabets.index(i.lower())].upper()
    else: # if any other character
      cipher += i
  return cipher

# this a function that will decrypt the message
def decrypt(cipher, key):
  text = ""
  for i in cipher:
    if (i in key):
      text += alphabets[key.index(i)]
    elif (i.isupper()): # if uppercase letter is there
      text += alphabets[key.index(i.lower())].upper()
    else: # if any other character
      text += i
  return text

# Key, encryption, and decryption of message 1
encrypted1 = encrypt(message1, key)
decrypted1 = decrypt(encrypted1, key)

print("Key for message 1: " + key)
print("Encrypted message 1:")
print(encrypted1)
print("")
print("Decrypted message 1:")
print(decrypted1)

print("")
print("")

# randomize key
key = ''.join(random.sample(alphabets,len(alphabets)))

# Key, encryption, and decryption of message 2
encrypted2 = encrypt(message2, key)
decrypted2 = decrypt(encrypted2, key)

print("Key for message 2: " + key)
print("Encrypted message 2:")
print(encrypted2)
print("")
print("Decrypted message 2:")
print(decrypted2)

print("")
print("")

# randomize key
key = ''.join(random.sample(alphabets,len(alphabets)))

# Key, encryption, and decryption of message 3
encrypted3 = encrypt(message3, key)
decrypted3 = decrypt(encrypted3, key)

print("Key for message 3: " + key)
print("Encrypted message 3:")
print(encrypted3)
print("")
print("Decrypted message 3:")
print(decrypted3)

print("Time to input your message in")

keepGoing = "y"
inputedMessage = ""

# Input message for encryption and decryption
while keepGoing == "y":
  # Input message
  x = input("Type in your message for encryption: ")
  inputedMessage = x

  # randomize key
  key = ''.join(random.sample(alphabets,len(alphabets)))

  # Key, encryption, and decryption of inputeed message
  encrypted = encrypt(inputedMessage, key)
  decrypted = decrypt(encrypted, key)

  print("Key for inputted message: " + key)
  print("Encrypted message:")
  print(encrypted)
  print("")
  print("Decrypted message:")
  print(decrypted)

  print("")
  x = input("Want to put another message(y/n)?: ")
  keepGoing = str(x)
