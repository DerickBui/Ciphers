# imports library of english words and methods
import enchant
# imports library to use math random functions
import random
# check the use of letter e and dictionary
d = enchant.Dict("en_US")

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # a normal alphabet
key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # use for modification


# length of alphabets is 26, stores sentences and keys
bruteForceStorage1 = [0] * len(alphabets)
bruteForceStorageKeys1 = [0] * len(alphabets)
bruteForceStorage2 = [0] * len(alphabets)
bruteForceStorageKeys2 = [0] * len(alphabets)
bruteForceStorage3 = [0] * len(alphabets)
bruteForceStorageKeys3 = [0] * len(alphabets)
bruteForceStorage4 = [0] * len(alphabets)
bruteForceStorageKeys4 = [0] * len(alphabets)

# Ciphers---------------------------------------------
cipher1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"

cipher2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"

cipher3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"

cipher4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

# FUNCTIONS-------------------------------------------
# this a function that will encrypt the message

# Create a dictionary of bigrams
# Text file taken online
bigramScore = {}
with open("bigrams.txt") as f:
  for i in f:
    (onekey, value) = i.split()
    bigramScore[onekey] = int(value)

# Function that scores what best fits according to bigramScore
def scoring(changedCipher):
  score = 0
  for i in range(len(changedCipher) - 1):
    if changedCipher[i:i+2] in bigramScore:
      score = score + bigramScore[changedCipher[i:i+2]]
    else:
      score = score + (-11.63)
  return score

# this a function that will encrypt the message
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

# this a function that will decrypt the message
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

# this function brute forces all possible combinations
def bruteForce(cipher, storeKey, key):
  print("Caesar ciphering")
  bruteForceStorage = [0] * len(alphabets)
  for i in range(len(alphabets)):
    print("Caesar Ciphering " + str(i + 1))
    bruteForceStorage[i] = decrypt(cipher, key)
    storeKey[i] = key
    key = key[1:] + key[0] # shift key by one left
  print("Caesar ciphering finished")
  return bruteForceStorage

# this function finds correct key from brute force decrypt
def findCorrectKey(bruteForceStorage, storeKey):
  print("Hill climb ciphering")
  markKey = 0
  finalWordCount = 0
  for i in range(len(bruteForceStorage)):
    wordCount = 0
    for j in range(len(bruteForceStorage[i]) - 5):
      if (d.check(bruteForceStorage[i][j:j + 5])):
        wordCount = wordCount + 1
    
    if (wordCount > finalWordCount):
      finalWordCount = wordCount
      markKey = i

  stringAndKey = [bruteForceStorage[markKey], str(storeKey[markKey])]
  return stringAndKey

# This function utilizes hill climbing algorithm to find key (not perfect as it relies too much on randomness)
def hillClimb(cipher):
  overallCounter = 0
  overallMessage = ""
  overallMaxScore = -99e9
  overallMaxPlayKey = list(key)

  maxScore = -99e9
  maxPlayKey = list(key)

  while overallCounter != 30:
    
    print("Process " + str(overallCounter + 1) + " of 30 in progress")
    
    random.shuffle(maxPlayKey)

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
    
    overallCounter = overallCounter + 1

  stringAndKey = [overallMessage, overallMaxPlayKey]
  return stringAndKey

# Find key most fit
def mostFit(caesar, hC):
  if len(caesar[0]) < 95:
    return caesar

  cScore = 0
  for i in range(len(caesar[0]) - 5):
    if (d.check(caesar[0][i:i + 5])):
      cScore = cScore + 1

  hScore = 0
  for i in range(len(hC[0]) - 5):
    if (d.check(hC[0][i:i + 5])):
      hScore = hScore + 1

  if cScore >= hScore:
    return caesar
  else:
    return hC


# # Function that returns ordered dictionary of combination frequency by greatest to least
# def orderLetFreqDict(letterFreq):
#   incrNum = 1
#   orderedDict = {}
#   for i in reversed(sorted(letterFreq, key=letterFreq.get)):
#     orderedDict[incrNum] = i
#     incrNum = incrNum + 1

#   return orderedDict

# # Function that counts character frequency
# def oneLetFreqCheck(cipherNS):
#   charCount = {}
#   for i in cipherNS:
#     if (i in charCount):
#       charCount[i] = charCount[i] + 1
#     else:
#       charCount[i] = 1
#   return charCount

# # Function that finds the most frequent two letters
# def twoLetFreqCheck(cipherNS):
#   threeFreq = {}
#   for i in range(len(cipherNS)-2):
#     if (cipherNS[i:i+2] in threeFreq):
#       threeFreq[cipherNS[i:i+2]] = threeFreq[cipherNS[i:i+2]] + 1
#     else:
#       threeFreq[cipherNS[i:i+2]] = 1
  
#   return threeFreq

# # Function that finds the most frequent three letters
# def threeLetFreqCheck(cipherNS):
#   threeFreq = {}
#   for i in range(len(cipherNS)-2):
#     if (cipherNS[i:i+3] in threeFreq):
#       threeFreq[cipherNS[i:i+3]] = threeFreq[cipherNS[i:i+3]] + 1
#     else:
#       threeFreq[cipherNS[i:i+3]] = 1
  
#   return threeFreq

# Cipher 1--------------------------------------------------------
# Create sentence with no spaces
cipher1NS = ""
for i in cipher1:
  if i != ' ':
    cipher1NS = cipher1NS + i

# Capitalize letters
cipher1NS = cipher1NS.upper()

print("------------------Cipher 1------------------")

# brute force encrypted message 1
bruteForceStorage1 = bruteForce(cipher1NS, bruteForceStorageKeys1, key)

# finds best fit key
bestFit1 = mostFit(findCorrectKey(bruteForceStorage1, bruteForceStorageKeys1), hillClimb(cipher1NS))

print("Most fit key of cipher 1: " + str("".join(bestFit1[1])))
print("Resulting sentence: " + str(bestFit1[0]))

# Cipher 2--------------------------------------------------------
# Create sentence with no spaces
cipher2NS = ""
for i in cipher2:
  if i != ' ':
    cipher2NS = cipher2NS + i

# Capitalize letters
cipher2NS = cipher2NS.upper()

print("------------------Cipher 2------------------")

#brute force encrypted message 2
bruteForceStorage2 = bruteForce(cipher2.upper(), bruteForceStorageKeys2, key)

# finds best fit key
bestFit2 = mostFit(findCorrectKey(bruteForceStorage2, bruteForceStorageKeys2), hillClimb(cipher2NS))

print("Most fit key of cipher 2: " + str("".join(bestFit2[1])))
print("Resulting sentence: " + str(bestFit2[0]))

# Cipher 3--------------------------------------------------------
# Create sentence with no spaces
cipher3NS = ""
for i in cipher3:
  if i != ' ':
    cipher3NS = cipher3NS + i

# Capitalize letters
cipher3NS = cipher3NS.upper()

print("------------------Cipher 3------------------")

#brute force encrypted message 3
bruteForceStorage3 = bruteForce(cipher3.upper(), bruteForceStorageKeys3, key)

# finds best fit key
bestFit3 = mostFit(findCorrectKey(bruteForceStorage3, bruteForceStorageKeys3), hillClimb(cipher3NS))

print("Most fit key of cipher 3: " + str("".join(bestFit3[1])))
print("Resulting sentence: " + str(bestFit3[0]))

# Cipher 4--------------------------------------------------------
# Create sentence with no spaces
cipher4NS = ""
for i in cipher4:
  if i != ' ':
    cipher4NS = cipher4NS + i

# Capitalize letters
cipher4NS = cipher4NS.upper()

print("------------------Cipher 4------------------")

#brute force encrypted message 4
bruteForceStorage4 = bruteForce(cipher4.upper(), bruteForceStorageKeys4, key)

# finds best fit key
bestFit4 = mostFit(findCorrectKey(bruteForceStorage4, bruteForceStorageKeys4), hillClimb(cipher4NS))

print("Most fit key of cipher 4: " + str("".join(bestFit4[1])))
print("Resulting sentence: " + str(bestFit4[0]))


