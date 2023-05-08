## TASK 2.1
print("TASK 2.1")
def SomeSort(SomeList):
    # from 1 to NumberOfItems - 1 (since Python is 0-based)
    NumberOfItems = len(SomeList)
    for Pointer in range(1, NumberOfItems):
        ItemToBeInserted = SomeList[Pointer]
        CurrentItem = Pointer - 1
        while (SomeList[CurrentItem] > ItemToBeInserted and CurrentItem > -1):
            SomeList[CurrentItem + 1] = SomeList[CurrentItem]
            CurrentItem -= 1
        SomeList[CurrentItem + 1] = ItemToBeInserted
    return SomeList

Numbers = [435,646,344,54,23,98,789,212,847,201,733]
print("Numbers array before SomeSort is run: ")
print(Numbers)
Numbers = SomeSort(Numbers)
print("\nNumbers array after SomeSort is run: ")
print(Numbers)

## TASK 2.2
print("\nTASK 2.2")
def BubbleSort(Array):
    for i in range(len(Array)):
        for j in range(len(Array) - 1):
            if Array[j] > Array[j + 1]:
                temp = Array[j]
                Array[j] = Array[j + 1]
                Array[j + 1] = temp
    return Array

Numbers = [435,646,344,54,23,98,789,212,847,201,733]
print("Numbers array before BubbleSort is run: ")
print(Numbers)
Numbers = SomeSort(Numbers)
print("\nNumbers array after BubbleSort is run: ")
print(Numbers)

## TASK 2.3
print("\nTASK 2.3")
def SomeSortM(SomeList):
    Comparisons = 0
    # from 1 to NumberOfItems - 1 (since Python is 0-based)
    NumberOfItems = len(SomeList)
    for Pointer in range(1, NumberOfItems):
        ItemToBeInserted = SomeList[Pointer]
        CurrentItem = Pointer - 1
        Comparisons += 1
        while (SomeList[CurrentItem] > ItemToBeInserted and CurrentItem > -1):
            SomeList[CurrentItem + 1] = SomeList[CurrentItem]
            CurrentItem -= 1
            Comparisons += 1
        SomeList[CurrentItem + 1] = ItemToBeInserted
    return (SomeList, Comparisons)

Numbers = [435,646,344,54,23,98,789,212,847,201,733]
print("Numbers array before SomeSortM is run: ")
print(Numbers)
Numbers, Comparisons = SomeSortM(Numbers)
print("\nNumbers array after SomeSortM is run: ")
print(Numbers)
print()
print("Number of comparisons using SomeSortM:", Comparisons)
print()

def BubbleSortM(Array):
    Comparisons = 0
    for i in range(len(Array)):
        for j in range(len(Array) - 1):
            Comparisons += 1
            if Array[j] > Array[j + 1]:
                temp = Array[j]
                Array[j] = Array[j + 1]
                Array[j + 1] = temp
    return (Array, Comparisons)

Numbers = [435,646,344,54,23,98,789,212,847,201,733]
print("Numbers array before BubbleSortM is run: ")
print(Numbers)
Numbers, Comparisons = BubbleSortM(Numbers)
print("\nNumbers array after BubbleSortM is run: ")
print(Numbers)
print()
print("Number of comparisons using BubbleSortM:", Comparisons)
