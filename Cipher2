def encrypt(plaintext, key):
  encrypted = ""
  for i in plaintext:
    if i.isupper():
      encrypted += chr((ord(i) + key - ord('A')) % 26 + ord('A'))
    elif i.islower():
      encrypted += chr((ord(i) + key - ord('a')) % 26 + ord('a'))
    else:
      encrypted += i
  return encrypted
