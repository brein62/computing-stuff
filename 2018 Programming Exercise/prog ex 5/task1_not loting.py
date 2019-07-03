def findMax(numberList):
    currentHighest = numberList[0]
    for i in numberList:
        if i > currentHighest:
            currentHighest = i
    return currentHighest

def findMin(numberList):
    currentLowest = numberList[0]
    for i in numberList:
        if i < currentLowest:
            currentLowest = i
    return currentLowest

def findAverage(numberList):
    total = 0
    for i in numberList:
        total += i
    return total/len(numberList)

numberFile = open("NUMBERS.txt", "r")
numbers=numberFile.read().split(" ")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numberFile.close()
print("Maximum number:", findMax(numbers))
print("Minimum number:", findMin(numbers))
print("Average number:", findAverage(numbers))

newFile = open("NEWFILE.txt", "w")
newFile.write("Maximum number: " + str(findMax(numbers)))
newFile.write("\nMinimum number: " + str(findMin(numbers)))
newFile.write("\nAverage number: " + str(findAverage(numbers)))
newFile.close()
