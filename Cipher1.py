alphabets = "abcdefghijklmnopqrstuvwxyz" # a normal alphabet
key = "lmnopqrstuvwxyzabcdefghijk" # a modified alphabet that is shifted by 11
message = "He who fights with monsters should look to it that he himself does not become a monster . And if you gaze long into an abyss , the abyss also gazes into you ."

# this a function that will encrypt the message
def encrypt(message, key):
  cipher = ""
  for i in message:
    if (i in key):
      cipher += key[alphabets.index(i)]
    elif (i.isupper()): # if uppercase letter is there
      cipher += key[alphabets.index(i.lower())].upper()
    else: # if any other character is there
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
    else:
      text += i
  return text

encryptedMessage = encrypt(message, key)
decryptedMessage = decrypt(encryptedMessage, key)


print(encryptedMessage)
print(decryptedMessage)
