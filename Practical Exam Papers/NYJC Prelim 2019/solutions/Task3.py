## TASK 3.1

class Node:
    def __init__(self, key = 0, left = None, right = None):   # constructor()
        self.__key   = int(key)
        self.__left  = left
        self.__right = right

    def insert(self, key = 0):
        self.__key   = int(key)

    def GetKey(self):
        return self.__key

    def SetLeft(self, left = None):
        self.__left = left

    def GetLeft(self):
        return self.__left

    def SetRight(self, right = None):
        self.__right = right

    def GetRight(self):
        return self.__right

class Tree:
    def __init__(self):                         # constructor()
        self.__Root = None

    def add(self, newItem = 0):
        newItem = int(newItem)
        newNode = Node(newItem, None, None)
        if self.__Root == None:   # binary tree is empty
            self.__Root = newNode
        else:
            previous = self.__Root
            current  = self.__Root
            lastmove = "X"
            while current != None:
                previous = current
                if newItem < current.GetKey():
                    current = current.GetLeft()
                    lastmove = "L"
                else:
                    current = current.GetRight()
                    lastmove = "R"
            if lastmove == "L":
                previous.SetLeft(newNode)
            else:
                previous.SetRight(newNode)

    def printTreeInOrder(self):
        self.printTreeInOrderFromIndex(self.__Root)
    
    def printTreeInOrderFromIndex(self, current):
        if current != None:
            self.printTreeInOrderFromIndex(current.GetLeft())
            print(current.GetKey())
            self.printTreeInOrderFromIndex(current.GetRight())

    ## TASK 3.5
    def FindKthSmallest(self, K):
        self.__count = 0        # the temp variable to be used
        return self.FindKthSmallestFromIndex(self.__Root, K)
        
    def FindKthSmallestFromIndex(self, current, K):
        if current != None:
            self.FindKthSmallestFromIndex(current.GetLeft(), K)
            self.__count += 1
            if self.__count == K:
                print("The {0}th smallest element in the binary tree is {1}.".format(K, current.GetKey()))
                print()
            self.FindKthSmallestFromIndex(current.GetRight(), K)

a = Tree()
a.add(15)
a.add(10)
a.add(20)
a.add(8)
a.add(12)
a.add(18)
a.add(25)
a.printTreeInOrder()
                    
## TASK 3.2
def CreateTreeFromArray(array):
    IntegerTree = Tree()
    for number in array:
        IntegerTree.add(int(number))
    IntegerTree.printTreeInOrder()
    return IntegerTree

BSTArray = [11, 6, 1, 14, 16, 7, 17, 20, 13, 9, 15, 8, 5, 4, 2]
CreateTreeFromArray(BSTArray)

## TASK 3.3
# add to integer tree - binary search style
def AddToIntegerTree(array, IntegerTree, lo, hi):
    if lo <= hi:
        mid = int((lo + hi) / 2)
        IntegerTree.add(array[mid])
        AddToIntegerTree(array, IntegerTree, lo, mid - 1)
        AddToIntegerTree(array, IntegerTree, mid + 1, hi)
    
def CreateTreeFromArray2(array):
    # perform a bubble sort
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                
    array2 = []
    lo = 0
    hi = len(array) - 1
    IntegerTree = Tree()
    AddToIntegerTree(array, IntegerTree, lo, hi)
    IntegerTree.printTreeInOrder()
    return IntegerTree

BSTArray = [11, 6, 1, 14, 16, 7, 17, 20, 13, 9, 15, 8, 5, 4, 2]
BSTTree  = CreateTreeFromArray2(BSTArray)
BSTTree.FindKthSmallest(5)
        
