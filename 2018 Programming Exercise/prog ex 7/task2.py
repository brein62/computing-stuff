#NOTE: pseudocode of insertion sort algorithm is 1-based.
def InsertionSort(array):                   #array is the list used in the insertion sort algorithm.
    for j in range(1, len(array)):          #looks from the 
        i = j - 1   
        temp = array[j]
        while i >= 0 and temp < array[i]:
            array[i + 1] = array[i]         #swaps adjacent elements until temp > array[i]
            i -= 1                          #i decreases until temp > array[i]
        array[i + 1] = temp                 #do not have a return value as this is stated to be a procedure
                                            #can put the print stmt here
                                            #but you know
                                            #array wil change anyway
PIE = [None] * 9
PIE[0]="Raspberry pie"
PIE[1]="Fish pie"
PIE[2]="Curry pie"
PIE[3]="Bumbleberry pie"
PIE[4]="Pumpkin pie"
PIE[5]="Bean pie"
PIE[6]="Apple pie"
PIE[7]="Strawberry pie"
PIE[8]="Meat pie"
print(PIE)
InsertionSort(PIE)
print(PIE)
