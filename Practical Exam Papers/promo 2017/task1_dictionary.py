# ----- TASK 1.1 -----
WordFile = open("WORDS1.txt", "r")
WordDict = dict()
HighestNo = 0                       #contains the current highest no of occurrences
for EachWord in WordFile:
    if EachWord[-1] == "\n":        #not the last line
        WordLine = EachWord[:-1].split(",")
    else:
        WordLine = EachWord.split(",")
    WordDict[WordLine[0]] = int(WordLine[1]) #dictionary entry ([word] ==> number)
    if int(WordLine[1]) > HighestNo:
        HighestNo = int(WordLine[1])

WordFile.close()

WordArray = list(WordDict.keys())       #array containing all terms
NumberArray = list(WordDict.values())   #array containg all the number of occurrences
for i in range(len(NumberArray)):
    if NumberArray[i] == HighestNo:
        HighestIndex = i
        break


print("The term containing the highest number of occurrences, with {}, is {}.".format(HighestNo, WordArray[HighestIndex]))

print()
print("-" * 80)
print()

# ----- TASK 1.2 -----
WordFile = open("WORDS2.txt", "r")
WordDict = dict()
HighestNo = 0                           #contains the current highest no of occurrences
for EachWord in WordFile:
    WordLine = EachWord[:-1]            #the word line is never the last line
    NumberLine = WordFile.readline()    #readline again to get the next line
    if NumberLine[-1] == "\n":         #not the last line
        NumberLine = NumberLine[:-1]
    WordDict[WordLine] = int(NumberLine) #dictionary entry ([word] ==> number)
    if int(NumberLine) > HighestNo:
        HighestNo = int(NumberLine)

WordFile.close()

WordArray = list(WordDict.keys())       #array containing all terms
NumberArray = list(WordDict.values())   #array containg all the number of occurrences
HighestIndices = []                     #array containing the index of all the highest occurrences
for i in range(len(NumberArray)):
    if NumberArray[i] == HighestNo:
        HighestIndices.append(i)

print("The terms containing the highest number of occurrences, with {}, are:".format(HighestNo))
for i in HighestIndices:
    print(WordArray[i])
