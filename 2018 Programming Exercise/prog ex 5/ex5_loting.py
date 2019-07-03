def findMax(numberList):
    currentHighest = -10000000000000
    for i in numberList:
        if i > currentHighest:
            currentHighest = i
    return currentHighest

def findMin(numberList):
    currentLowest= 10000000000000000
    for i in numberList:
        if i < currentLowest:
            currentLowest = i
    return currentLowest

def findAverage(numberList):
    s = 0
    for i in numberList:
        s += i
    return s/len(numberList)
        
file=open("NUMBERS.txt","r")
NumberArray=[]
numberstr=file.readline()
numberArray=numberstr.split(" ")
print(numberArray)
