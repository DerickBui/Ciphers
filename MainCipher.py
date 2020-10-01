#imports library of english words
import enchant
#check the use of letter e and dictionary
d = enchant.Dict("en_US")

alphabets = "abcdefghijklmnopqrstuvwxyz" # a normal alphabet
key = "bcdefghijklmnopqrstuvwxyza" # a modified alphabet that is shifted by 1

# Information-------------------------------------------
# estimated frequency of letters from most to least
mostCommon = "ETAOINSHRDLUCMWFYGPBVKXJQZ"

# Most common double letter combinations
doubleComb = {1 : "SS", 2 : "EE", 3 : "TT", 4 : "FF", 5 : "LL", 6 : "MM", 7 : "OO"}

# Most common three letter combinations
threeComb = {1 : "THE", 2 : "AND", 3 : "THA:", 4 : "ENT", 5 : "ION", 6 : "TIO", 7 : "FOR", 8 : "NDE", 9 : "HAS", 10 : "NCE", 11 : "TIS", 12 : "OFT", 13 : "MEN"}

# Most common two letter combinations
twoComb = {1 : "TH", 2 : "HE", 3 : "AN", 4 : "IN", 5 : "ER", 6 : "ON", 7 : "RE", 8 : "ED", 9 : "ND", 10 : "HA", 11 : "AT", 12 : "EN"}

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

# Cipher 3--------------------------------------------------------
cipher3NS = ""
for i in cipher3:
  if i != ' ':
    cipher3NS = cipher3NS + i

message3 = ""


# Check most frequent letter in order from greatest to least
orderedOneLetterFreq = orderLetFreqDict(oneLetFreqCheck(cipher3NS))

# Check most frequent 2 letters in order from greatest to least
orderedTwoLetterFreq = orderLetFreqDict(twoLetFreqCheck(cipher3NS))

# Check most frequent 3 letters in order from greatest to least
orderedThreeLetterFreq = orderLetFreqDict(threeLetFreqCheck(cipher3NS))

# Gets the most frequent 3 letter combination
mostFreq3Let = orderedThreeLetterFreq[1]

# check letter clash for e
if not clashLetCheck(orderedOneLetterFreq[1], mostCommon[0]): # if not clash
  subLetters[orderedOneLetterFreq[1]] = mostCommon[0] # q = e

# check 3 letter clash for shq and the
clashed = False
for i in range(len(orderedThreeLetterFreq[1])):
  if clashLetCheck(orderedThreeLetterFreq[1][i], threeComb[1][i]): # if clash
    clashed = True
    break
  else: # No clash
    print("False")


if not clashed: # If no clashes
  for i in range(len(orderedThreeLetterFreq[1])):
    subLetters[orderedThreeLetterFreq[1][i]] = threeComb[1][i]

for i in range(len(mostCommon)):
  if mostCommon[i] not in subLetters.values(): # Continue if letter not assigned
    for j in orderedOneLetterFreq: # Goes through each orderedOneLetterFreq
      if not clashLetCheck(orderedOneLetterFreq[j], mostCommon[i]): # Continue if letter not clashing
        subLetters[orderedOneLetterFreq[j]] = mostCommon[i]
        break

for i in range(len(cipher3NS)):
  if subLetters[cipher3NS[i]] != None:
    message3 = message3 + subLetters[cipher3NS[i]]
  else:
    message3 = message3 + cipher3NS[i]

print(message3)

# Cipher 4--------------------------------------------------------
# Cipher4 No Space

# Reset substituted letters
for i in subLetters:
  subLetters[i] = None

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
if not clashLetCheck(orderedOneLetterFreq[1], mostCommon[0]): # if not clash
  subLetters[orderedOneLetterFreq[1]] = mostCommon[0] # q = e

# check 3 letter clash for shq and the
clashed = False
for i in range(len(orderedThreeLetterFreq[1])):
  if clashLetCheck(orderedThreeLetterFreq[1][i], threeComb[1][i]): # if clash
    clashed = True
    break
  else: # No clash
    print("False")


if not clashed: # If no clashes
  for i in range(len(orderedThreeLetterFreq[1])):
    subLetters[orderedThreeLetterFreq[1][i]] = threeComb[1][i]

for i in range(len(mostCommon)):
  if mostCommon[i] not in subLetters.values(): # Continue if letter not assigned
    for j in orderedOneLetterFreq: # Goes through each orderedOneLetterFreq
      if not clashLetCheck(orderedOneLetterFreq[j], mostCommon[i]): # Continue if letter not clashing
        subLetters[orderedOneLetterFreq[j]] = mostCommon[i]
        break

for i in range(len(cipher4NS)):
  if subLetters[cipher4NS[i]] != None:
    message4 = message4 + subLetters[cipher4NS[i]]
  else:
    message4 = message4 + cipher4NS[i]

print(subLetters)

print(message4)


