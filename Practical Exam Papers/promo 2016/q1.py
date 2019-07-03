raceData = open("RACE.txt", "r")
raceArray = []              #store race data in a 2-D array
for eachRacer in raceData:
    racerData = eachRacer[:-1].split(",")
    runnerID = racerData[0]
    countryCode = racerData[1]
    runnerName = racerData[2]
    raceTime = racerData[3]
    raceArray.append(racerData)

print("|{0:^15}|{1:^10}|{2:^20}|{3:^15}".format("Runner ID", "Country", "Name", "Race Time"))
print("-"*73)
sortedRaceArray = raceArray                                             #for bubble sorting

###a simple bubble sort algorithm (can use insertion sort, quick sort, etc.)
##i = 1
##while i < len(sortedRaceArray):
##    for racer in range(len(sortedRaceArray) - 1):
##        if sortedRaceArray[racer][3] > sortedRaceArray[racer + 1][3]:        #if faster, swap.
##            temp = sortedRaceArray[racer]
##            sortedRaceArray[racer] = sortedRaceArray[racer + 1]
##            sortedRaceArray[racer + 1] = temp
##    i += 1

#insertion sort (thanks mr ng)
for i in range(len(sortedRaceArray)):
    x = sortedRaceArray[i]
    j = i
    while j > 0 and sortedRaceArray[j - 1][3] > x[3]:
        sortedRaceArray[j] = sortedRaceArray[j - 1]
        j = j - 1
    sortedRaceArray[j] = x

for eachRacer in range(10):
    print("|{0:^15}|{1:^10}|{2:^20}|{3:^15}".format(sortedRaceArray[eachRacer][0], sortedRaceArray[eachRacer][1], sortedRaceArray[eachRacer][2], sortedRaceArray[eachRacer][3]))
        
raceData.close()
