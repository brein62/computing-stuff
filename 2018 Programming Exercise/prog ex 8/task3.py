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

# prints output depending on whether item is found or not
def search(data, toFind, start, end):
    
    # the search result
    result = Recursive_binary_search(data, toFind, start, end)
    if result == -1:
        print("Item", toFind, "is not found.")
    else:
        print("The index of the item {} in the array is {}.".format(toFind, result))


def main():
    scoreFile = open("newscore.txt","r")
    score=scoreFile.read().split(",")
    for i in range(len(score)):
        score[i] = int(score[i])
    scoreFile.close()
    search(score, 569, 0, len(score) - 1)

main()