#NOTE: pseudocode of insertion sort algorithm is 1-based.
WOOD = [None for i in range(17)]
WOOD[0]="Cedar"
WOOD[1]="Cypress"
WOOD[2]="Pine"
WOOD[3]="Fir"
WOOD[4]="Redwood"
WOOD[5]="Alder"
WOOD[6]="Basswood"
WOOD[7]="Birch"
WOOD[8]="Chestnut"
WOOD[9]="Elm"
WOOD[10]="Hickory"
WOOD[11]="Mahogany"
WOOD[12]="Maple"
WOOD[13]="Merbau"
WOOD[14]="Oak"
WOOD[15]="Teak"
WOOD[16]="Bamboo"
print("Original: ", WOOD)
for j in range(1, len(WOOD)):
    i = j - 1                           #i, j refers to an index of an array
    temp = WOOD[j]
    while i >= 0 and temp < WOOD[i]:
        WOOD[i + 1] = WOOD[i]         #swaps adjacent elements until temp > array[i]
        i -= 1                          #i decreases until temp > array[i]
    WOOD[i + 1] = temp
print("Converted:", WOOD)
