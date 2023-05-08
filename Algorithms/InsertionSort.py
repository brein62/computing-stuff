def InsertionSort(ar):
    for i in range(1, len(ar)):
        j = i - 1
        temp = ar[j + 1]
        while j >= 0 and temp < ar[j]:
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = temp
    return ar

import random
array = [random.randint(1, 100) for i in range(100)]

def PrintAndSort(array):
    # before operating quick sort
    print("Before operating insertion sort: ")
    print(array)
    InsertionSort(array)
    # after operating quick sort
    print("After operating insertion sort: ")
    print(array)

PrintAndSort(array)
