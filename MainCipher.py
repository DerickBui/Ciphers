#imports library of english words
import enchant
#check the use of letter e and dictionary
d = enchant.Dict("en_US")

alphabets = "abcdefghijklmnopqrstuvwxyz" # a normal alphabet
key = "bcdefghijklmnopqrstuvwxyza" # a modified alphabet that is shifted by 1

# Information-------------------------------------------
# estimated frequency of letters from most to least
mostCommon = "etaoinshrdlucmwfygpbvkxjqz"

# Most common double letter combinations
doubleComb = {1 : "ss", 2 : "ee", 3 : "tt", 4 : "ff", 5 : "ll", 6 : "mm", 7 : "oo"}

# Most common three letter combinations
threeComb = {1 : "the", 2 : "and", 3 : "tha:", 4 : "ent", 5 : "ion", 6 : "tio", 7 : "for", 8 : "nde", 9 : "has", 10 : "nce", 11 : "tis", 12 : "oft", 13 : "men"}

# Most common two letter combinations
twoComb = {1 : "th", 2 : "he", 3 : "an", 4 : "in", 5 : "er", 6 : "on", 7 : "re", 8 : "ed", 9 : "nd", 10 : "ha", 11 : "at", 12 : "en"}

#For assigning letters
subLetters = {'a':None, 'b':None, 'c':None, 'd':None, 'e':None, 'f':None, 'g':None, 'h':None, 'i':None, 'j':None, 'k':None, 'l':None, 'm':None, 'n':None, 'o':None, 'p':None, 'q':None, 'r':None, 's':None, 't':None, 'u':None, 'v':None, 'w':None, 'x':None, 'y':None, 'z':None}

# length of alphabets is 26
bruteForceStorage1 = [0] * len(alphabets)
bruteForceStorage2 = [0] * len(alphabets)
bruteForceStorage3 = [0] * len(alphabets)
bruteForceStorage4 = [0] * len(alphabets)

# Ciphers---------------------------------------------
cipher1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"

cipher2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"

cipher3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"

cipher4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

# FUNCTIONS-------------------------------------------
# this a function that will encrypt the message
def encrypt(message, key):
  cipher = ""
  for i in message:
    if (i in key):
      cipher += key[alphabets.index(i)]
    elif (i.isupper()): # if uppercase letter is there
      cipher += key[alphabets.index(i.lower())].upper()
    elif (i != " "): # if any other character is there beside spaces
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
    elif (i != i): # if any other character is there beside spaces
      text += i
  return text

# this function brute forces all possible combinations
def bruteForce(cipher, key):
  bruteForceStorage = [0] * len(alphabets) 
  for i in range(len(alphabets)):
    bruteForceStorage[i] = decrypt(cipher, key)
    print(str(i+1) + ". " + bruteForceStorage[i])
    key = key[1:] + key[0] # shift key by one left
  return bruteForceStorage

# this function finds correct key from brute force decrypt
def findCorrectKey(bruteForceStorage):
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

  print("")
  print("Message in key " + str(markKey + 1) + ": " + bruteForceStorage[markKey])
  print("")

# Function that returns ordered dictionary of combination frequency by greatest to least
def orderLetFreqDict(letterFreq):
  incrNum = 1
  orderedDict = {}
  for i in reversed(sorted(letterFreq, key=letterFreq.get)):
    orderedDict[incrNum] = i
    incrNum = incrNum + 1

  return orderedDict

# Function that counts character frequency
def oneLetFreqCheck(cipherNS):
  charCount = {}
  for i in cipherNS:
    if (i in charCount):
      charCount[i] = charCount[i] + 1
    else:
      charCount[i] = 1
  return charCount

# Function that finds the most frequent two letters
def twoLetFreqCheck(cipherNS):
  threeFreq = {}
  for i in range(len(cipherNS)-2):
    if (cipherNS[i:i+2] in threeFreq):
      threeFreq[cipherNS[i:i+2]] = threeFreq[cipherNS[i:i+2]] + 1
    else:
      threeFreq[cipherNS[i:i+2]] = 1
  
  return threeFreq

# Function that finds the most frequent three letters
def threeLetFreqCheck(cipherNS):
  threeFreq = {}
  for i in range(len(cipherNS)-2):
    if (cipherNS[i:i+3] in threeFreq):
      threeFreq[cipherNS[i:i+3]] = threeFreq[cipherNS[i:i+3]] + 1
    else:
      threeFreq[cipherNS[i:i+3]] = 1
  
  return threeFreq

# Function that checks on one letter clash, true if clash
# mostFreqLetChar -> character of selected mostFreqLet
# letCombChar -> character of selected letter combination
def clashLetCheck(mostFreqLetChar, letCombChar):
  # Check if letter clashes
  if letCombChar not in subLetters.values(): # Check if letter not assigned in subLetters
    if subLetters[mostFreqLetChar] != None: # If there is a letter assigned
      if subLetters[mostFreqLetChar] != letCombChar: # If assigned letter does not match
        return True # There is a clash
  else:
    if subLetters[mostFreqLetChar] != letCombChar:
      return True # There is a clash with another letter assigned

  return False

# Cipher 1--------------------------------------------------------
# length of alphabets is 26 for all for loops
# brute force encrypted message 1
bruteForceStorage1 = bruteForce(cipher1, key)

# finds correct key
findCorrectKey(bruteForceStorage1)

# Cipher 2--------------------------------------------------------
#brute force encrypted message 2
bruteForceStorage2 = bruteForce(cipher2, key)

# finds correct key
findCorrectKey(bruteForceStorage2)


# Cipher 4--------------------------------------------------------
# Cipher4 No Space
cipher4NS = ""
for i in cipher4:
  if i != ' ':
    cipher4NS = cipher4NS + i

message4 = ""


# Check most frequent letter in order from greatest to least
orderedOneLetterFreq = orderLetFreqDict(oneLetFreqCheck(cipher4NS))

# Check most frequent 2 letters in order from greatest to least
orderedTwoLetterFreq = orderLetFreqDict(twoLetFreqCheck(cipher4NS))

# Check most frequent 3 letters in order from greatest to least
orderedThreeLetterFreq = orderLetFreqDict(threeLetFreqCheck(cipher4NS))

print("")

# Gets the most frequent 3 letter combination
mostFreq3Let = orderedThreeLetterFreq[1]

# check letter clash for e
if not (clashLetCheck(mostCommon[0], orderedOneLetterFreq[1])):
  print("yeah")
  subLetters[mostCommon[0]] = orderedOneLetterFreq[1]

# check letter clash
for i in range(len(threeComb[1])):
  print(mostFreq3Let[i] + " " + threeComb[1][i])
  print(clashLetCheck(mostFreq3Let[i], threeComb[1][i]))

for i in range(len(mostFreq3Let)): # Add letters to subLetters
  subLetters[mostFreq3Let[i]] = threeComb[1][i]


# for i in range(len(cipher4NS)):
#   if subLetters[cipher4NS[i]] != None:
#     message4 = message4 + subLetters[cipher4NS[i]]
#   else:
#     message4 = message4 + cipher4NS[i]

# print(subLetters)

# print(message4)


