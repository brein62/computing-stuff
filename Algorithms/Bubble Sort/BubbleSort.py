##def BubbleSort(ar):
##    for i in range(len(ar)):             #each pass
##        for j in range(len(ar) - 1):     #to swap
##            if ar[j] > ar[j + 1]:
##                temp = ar[j + 1]
##                ar[j + 1] = ar[j]
##                ar[j] = temp



def BubbleSort(array):
    swapped = True
    while swapped == True:
        swapped = False
        for i in range(len(array) - 1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                swapped = True
            else:
                i = i + 1

a = [1,8,5,11,2,9,3,10,4]
BubbleSort(a)
