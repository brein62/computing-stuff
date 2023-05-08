InventoryFile = open("INVENTORY.TXT", "r")
Inventory = []      # a list holding all the inventory
for line in InventoryFile:
    # remove any newlines at the end of the line
    if line[-1] == "\n":
        line = line[:-1]

    Inventory.append(line)
    
InventoryFile.close()

ItemTypes = []      # a list holding all unique item types
for item in Inventory:
    if item not in ItemTypes:
        ItemTypes.append(item)
        
# a list holding all items of a certain type
ItemCounts = [0 for i in range(len(ItemTypes))]     
for i in range(len(ItemTypes)):
    count = 0
    for item in Inventory:
        if item == ItemTypes[i]:
            count += 1
    ItemCounts[i] = count

# print heading
print("{0:<20}{1}".format("ItemType", "Count"))
print()
for i in range(len(ItemTypes)):
    print("{0:<20}{1}".format(ItemTypes[i], ItemCounts[i]))
    
