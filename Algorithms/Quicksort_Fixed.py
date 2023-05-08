def QuickSort(Array):
    QuickSortHelper(Array, 0, len(Array) - 1)
    return Array

def QuickSortHelper(Array, First, Last):
    if First < Last:
        SplitPoint = Partition(Array, First, Last)
        QuickSortHelper(Array, First, SplitPoint - 1)
        QuickSortHelper(Array, SplitPoint + 1, Last)
    return Array

def Partition(Array, First, Last):
    PivotValue = Array[First]
    i = First + 1
    j = Last
    Done = False
    while Done == False:
        while i <= j and Array[i] <= PivotValue:
            i += 1
            
        while i <= j and Array[j] >= PivotValue:
            j -= 1
            
        if i > j:
            Done = True
        else:
            # swap Array[i], Array[j]
            Temp = Array[i]
            Array[i] = Array[j]
            Array[j] = Temp
    
    # swap Array[First], Array[j]
    Temp = Array[First]
    Array[First] = Array[j]
    Array[j] = Temp

    return j

import random
array = [random.randint(1, 100) for i in range(100)]

def PrintAndSort(array):
    # before operating quick sort
    print("Before operating quick sort: ")
    print(array)
    QuickSort(array)
    # after operating quick sort
    print("After operating quick sort: ")
    print(array)

PrintAndSort(array)
