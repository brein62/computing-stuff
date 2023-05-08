## TASK 1.1
## Evidence 1
def DisplayMenu():
    print("1. Read file data")
    print("2. Bubble sort")
    print("3. Quick sort / Insertion sort")
    print("4. End")

## TASK 1.2
## Evidence 1
def Option1():
    AdmissionsFile = open("ADMISSIONS-DATA.TXT", "r")
    AdmissionsList = []
    for line in AdmissionsFile:
        if line[-1] == "\n":
            line = line[:-1]
        line = int(line)
        AdmissionsList.append(line)
    AdmissionsFile.close()
    return AdmissionsList

## Evidence 2
def BubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array

## Evidence 3
def InsertionSort(array):
    for i in range(len(array)):
        ToInsert = array[i]
        j = i - 1
        while j >= 0 and ToInsert < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = ToInsert
    return array

# MAIN PROGRAM
option = ""
DisplayMenu()
print(BubbleSort(Option1()))
print(InsertionSort(Option1()))
