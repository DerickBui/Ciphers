import enchant
#check the use of letter e and dictionary
d = enchant.Dict("en_US")

print(d.check("here"))

alphabets = "abcdefghijklmnopqrstuvwxyz" # a normal alphabet
key = "bcdefghijklmnopqrstuvwxyza" # a modified alphabet that is shifted by 1
key = key[1:] + key[0]

# length of alphabets is 26
bruteForceStorage1 = [0] * len(alphabets)
bruteForceStorage2 = [0] * len(alphabets)
bruteForceStorage3 = [0] * len(alphabets)
bruteForceStorage4 = [0] * len(alphabets)

cipher1 = "fqjcb rwjwj vnjax bnkhj whxcq nawjv nfxdu mbvnu ujbbf nnc"

cipher2 = "oczmz vmzor jocdi bnojv dhvod igdaz admno ojbzo rcvot jprvi oviyv aozmo cvooj ziejt dojig toczr dnzno jahvi fdiyv xcdzq zoczn zxjiy"

cipher3 = "ejitp spawa qleji taiul rtwll rflrl laoat wsqqj atgac kthls iraoa twlpl qjatw jufrh lhuts qataq itats aittk stqfj cae"

cipher4 = "iyhqz ewqin azqej shayz niqbe aheum hnmnj jaqii yuexq ayqkn jbeuq iihed yzhni ifnun sayiz yudhe sqshu qesqa iluym qkque aqaqm oejjs hqzyu jdzqa diesh niznj jayzy uiqhq vayzq shsnj jejjz nshna hnmyt isnae sqfun dqzew qiead zevqi zhnjq shqze udqai jrmtq uishq ifnun siiqa suoij qqfni syyle iszhn bhmei squih nimnx hsead shqmr udquq uaqeu iisqe jshnj oihyy snaxs hqihe lsilu ymhni tyz"

message = "He who fights with monsters should look to it that he himself does not become a monster . And if you gaze long into an abyss , the abyss also gazes into you ."

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

# length of alphabets is 26 for all for loops
# brute force encrypted message 1
for i in range(len(alphabets)):
  bruteForceStorage1[i] = decrypt(cipher1, key)
  print(str(i+1) + ". " + bruteForceStorage1[i])
  key = key[1:] + key[0] # shift key by one left

markKey1 = 0
finalWordCount = 0
for i in range(len(bruteForceStorage1)):
  wordCount = 0
  for j in range(len(bruteForceStorage1[i]) - 5):
    if (d.check(bruteForceStorage1[i][j:j + 5])):
      # print("It's message: " + bruteForceStorage1[i])
      # break
      wordCount = wordCount + 1
  if (wordCount > finalWordCount):
    finalWordCount = wordCount
    markKey1 = i

print("Message in key " + str(markKey1 + 1) + ": " + bruteForceStorage1[markKey1])
print("")

#brute force encrypted message 2
for i in range(len(alphabets)):
  bruteForceStorage2[i] = decrypt(cipher2, key)
  print(str(i+1) + ". " + bruteForceStorage2[i])
  key = key[1:] + key[0] # shift key by one left


markKey2 = 0
finalWordCount = 0
for i in range(len(bruteForceStorage2)):
  wordCount = 0
  for j in range(len(bruteForceStorage2[i]) - 5):
    if (d.check(bruteForceStorage2[i][j:j + 5])):
      # print("It's message: " + bruteForceStorage1[i])
      # break
      wordCount = wordCount + 1
  if (wordCount > finalWordCount):
    finalWordCount = wordCount
    markKey2 = i

print("Message in key " + str(markKey1 + 1) + ": " + bruteForceStorage2[markKey2])
print("")

#brute force encrypted message 3
for i in range(len(alphabets)):
  print(decrypt(cipher3, key))
  key = key[1:] + key[0] # shift key by one left
