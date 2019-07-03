Max = 20
filename = input("Enter file name here: ")     
file = open(filename, "r")
Table = [None for i in range(Max)]
for line in file:
    if line[-1] == "\n":
        line = line[:-1]
    line = int(line)
    index = line % Max
    while Table[index] != None:
        if index == (Max - 1):
            index = 0
        else:
            index += 1
        
    Table[index] = line

print("-" * 57)
print("| {0:^10} | {1:^40} |".format("Hash", "Value"))
print("-" * 57)
for i in range(Max):
    if Table[i] != None:
        print("| {0:^10} | {1:^40} |".format(i, Table[i]))
    else:
        print("| {0:^10} | {1:^40} |".format(i, "None"))
print("-" * 57)
        
IDSearch = input("Enter an ID number: ")
IDSearch = int(IDSearch)
index = IDSearch % Max
count = 0
while count < Max and Table[index] != IDSearch:          # less than 1 loop done
    count += 1
    if index == (Max - 1):
        index = 0
    else:
        index += 1

if Table[index] == IDSearch:
    print("{0} is found at index {1} in the hash table.".format(IDSearch, index))
else:
    print("{0} is not found in the hash table.".format(IDSearch))
    
    
