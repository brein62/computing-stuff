##  Binary Search Algorithm.
##  INPUT:
## data is an array of integers SORTED in ASCENDING order,
##        toFind is the integer to search for,
##        start is the minimum array index,
##        end is the maximum array index
##  OUTPUT:
## position of the integer toFind within array data, -1 if not found
def Recursive_binary_search(data, toFind, start, end):
    mid = int((start + end) / 2)                                        #gets the middle index of the array
    if start > end:                                                     #when not found
        return -1
    elif data[mid] == toFind:                                           #data is found!
        return mid
    elif data[mid] > toFind:                                            #data is more than search key
        return Recursive_binary_search(data, toFind, start, mid - 1)    #left sub-array
    else:                                                               #data is less than search key
        return Recursive_binary_search(data, toFind, mid + 1, end)      #right sub-array

def main():
    scoreFile = open("newscore.txt","r")
    score=scoreFile.read().split(",")
    for i in range(len(score)):
        score[i] = int(score[i])
    scoreFile.close()
    search = Recursive_binary_search(score, 569, 0, len(score) - 1)
    if search == -1:
        print("Item {} is not found.".format(569))
    else:
        print("The index of the item {} in the array is {}.".format(569, search))

