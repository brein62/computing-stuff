wordFile = open("WORDS2.txt", "r")
wordArray = [] #a list containing all entries in WORDS2
currentHighestNo = 0 #the highest number of occurrences
for wordLine in wordFile: #every 2 lines since readline is also called
    wordLine = wordLine[:-1] #all lines with the term are not last line
    numberLine = wordFile.readline()
    if numberLine[-1] == "\n": #not the last line
        numberLine = numberLine[:-1]
    wordArray.append([wordLine, int(numberLine)])
        
    if int(numberLine) > currentHighestNo:
        currentHighestNo = int(numberLine)
wordFile.close()
print("The terms with the highest number of occurrences, with {} occurrences, are:".format(currentHighestNo))

for eachWord in wordArray:
    if eachWord[1] == currentHighestNo: #has highest occurrences
        print("-", eachWord[0])

