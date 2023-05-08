#Task 2.2
def BinarySearch(lst, item):
    first = 0
    last  = len(lst) - 1
    middle = 0
    ElementFound = False
    WordsExamined = []
    while last >= first and ElementFound == False:
        middle = int((first + last) / 2)
        WordsExamined.append(lst[middle])
        if item > lst[middle]:
            first = middle + 1
        elif item < lst[middle]:
            last = middle - 1
        else:
            ElementFound = True
    if ElementFound:
        print("The word, " + item + ", is found in the list at index " + str(middle) + ".")
    else:
        print("The word, " + item + ", is not found in the list.")
    print("Words examined:")
    for word in WordsExamined:
        print("-", word)
    print()

#Task 2.3
def BinarySearchM(lst, item):
    first = 0
    last  = len(lst) - 1
    middle = 0
    ElementFound = False
    WordsExamined = []
    while last >= first and ElementFound == False:
        middle = int((first + last) / 2)
        WordsExamined.append(lst[middle])
        if item > lst[middle]:
            first = middle + 1
        elif item < lst[middle]:
            last = middle - 1
        else:
            ElementFound = True
    index = first
    output = []
    while lst[index].startswith(item):
        output.append(lst[index])
        index += 1
    return output
        

WordsFile = open("1000WORDS.txt", "r")
dataset = []
for word in WordsFile:
    if word[-1] == "\n":
        word = word[:-1]
    dataset.append(word)

BinarySearch(dataset, "WORD")
BinarySearch(dataset, "WORDA")
BinarySearch(dataset, "TRADE")
print(BinarySearchM(dataset, "TR"))
print(BinarySearchM(dataset, "RE"))
        
