def ProcessFile(WordsFile = "WORDS1.TXT"):
    WordsFile = open(WordsFile, "r")
    word = "a"
    freq = "0"
    HighestWord = ""
    HighestFreq = -1
    while True:

        # read every 2 lines
        word = WordsFile.readline()
        freq = WordsFile.readline()

        # if end of the file is reached
        if word == "" or freq == "":
            break
        
        if word[-1] == "\n":
            word = word[:-1]
        if freq[-1] == "\n":
            freq = freq[:-1]
        freq = int(freq)
        if freq > HighestFreq:
            HighestWord = word
            HighestFreq = freq
            
    WordsFile.close()
    print("The term with the highest number of occurrences is {0}, with {1} occurrences.".format(HighestWord, HighestFreq))

def ProcessFileModified(WordsFile = "WORDS2.TXT"):
    WordsFile = open(WordsFile, "r")
    word = "a"
    freq = "0"
    HighestWord = []
    HighestFreq = -1
    while True:

        # read every 2 lines
        word = WordsFile.readline()
        freq = WordsFile.readline()

        # if end of the file is reached
        if word == "" or freq == "":
            break
        
        if word[-1] == "\n":
            word = word[:-1]
        if freq[-1] == "\n":
            freq = freq[:-1]
        freq = int(freq)
        if freq > HighestFreq:
            HighestWord = [word]
            HighestFreq = freq
        elif freq == HighestFreq:
            HighestWord.append(word)
    WordsFile.close()
    print("The term(s) with the highest number of occurrences, with {0} occurrences, are:".format(HighestFreq))
    for EachWord in HighestWord:
        print("-", EachWord)

print("TASK 1.1:")
ProcessFile("WORDS1.TXT")
print()
print("TASK 1.2:")
ProcessFileModified("WORDS2.TXT")
