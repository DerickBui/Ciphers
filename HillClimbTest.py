import random

cipher = "sohewaxesinwealthnowisecanharmhimillnessoragenoevilcaresshadowhisspiritnoswordhatethreatensfromeveranenemyalltheworldwendsathiswillnoworseheknowethtillallwithinhimobstinatepridewaxesandwakeswhilethewardenslumbersthespiritssentrysleepistoofastwhichmastershismightandthemurderernearsstealthilyshootingtheshaftsfromhisbow"
cipher = cipher.upper()

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # a normal alphabet
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # string to be modified
keyList = list(key)

bigramScore = {}
trigramScore = {}
quadgramScore = {}

with open("bigrams.txt") as f:
  for i in f:
    (onekey, value) = i.split()
    bigramScore[onekey] = int(value)

# print(math.log10(0.01/(sum(bigramScore.values()))))

with open("trigrams.txt") as f:
  for i in f:
    (onekey, value) = i.split()
    trigramScore[onekey] = int(value)

# print(math.log10(0.01/(sum(trigramScore.values()))))

# Make dictionary of from quadgram score for quick access
with open("quadgrams.txt") as f:
  for i in f:
    (onekey, value) = i.split()
    quadgramScore[onekey] = int(value)


def encrypt(message, key):
  cipher = ""
  for i in message:
    if (i in key):
      cipher += key[alphabets.index(i)]
    elif (i.lower()): # if uppercase letter is there
      cipher += key[alphabets.index(i.upper())].lower()
    elif (i != " "): # if any other character is there beside spaces
      cipher += i
  return cipher

def decrypt(cipher, key):
  text = ""
  for i in cipher:
    if (i in key):
      text += alphabets[key.index(i)]
    elif (i.islower()): # if uppercase letter is there
      text += alphabets[key.index(i.upper())].lower()
    elif (i != i): # if any other character is there beside spaces
      text += i
  return text

def scoring(changedCipher):
  score = 0
  for i in range(len(changedCipher) - 1):
    if changedCipher[i:i+2] in bigramScore:
      score = score + bigramScore[changedCipher[i:i+2]]
    else:
      score = score + (-11.63)
  return score

overallCounter = 0
overallMessage = ""
overallMaxScore = -99e9
overallMaxPlayKey = list(key)

maxScore = -99e9
maxPlayKey = list(key)

while overallCounter != 20:
  
  print("Process " + str(overallCounter + 1) + " of 20 in progress")
  
  random.shuffle(maxPlayKey)

  print("".join(maxPlayKey))
  print("")
  maxDecrypted = decrypt(cipher, maxPlayKey)
  maxScore = scoring(maxDecrypted)

  counter = 0
  while counter != 1000:
    # Switch 2 letters in key
    rand1 = 0
    rand2 = 0
    while rand1 == rand2: #To make sure numbers are not the same
      rand1 = random.randint(0,25)
      rand2 = random.randint(0,25)
    playKey = maxPlayKey[:] # Copy key by value

    # Switch Letters
    playKey[rand1], playKey[rand2] = playKey[rand2], playKey[rand1]

    decrypted = decrypt(cipher, playKey)

    score = scoring(decrypted)

    if score > maxScore:
      maxScore = score
      maxDecrypted = decrypted
      maxPlayKey = playKey
      counter = 0
    
    counter = counter + 1
  
  if maxScore > overallMaxScore:
    overallMaxScore = maxScore
    overallMaxPlayKey = maxPlayKey
    overallMessage = decrypt(cipher, overallMaxPlayKey)
    print(overallMessage)
    print("")
  else:
    print("Worse key")
    print("")
  
  overallCounter = overallCounter + 1

