## TASK 1.1

RainfallFile = open("RAINFALL.txt", "r")

# stores number of rainy days in each year:
# {year: number of rainy days}
RainfallDict = {}
RainfallFile.readline()             # exclude first line
for line in RainfallFile:
    if line[-1] == "\n":
        line = line[:-1]
    record = line.split(",")
    year   = int(record[0][0:4])    # current year
    rainy  = int(record[1])         # number of rainy days in a month

    # if year is not in dict
    if year not in RainfallDict.keys():
        RainfallDict[year] = rainy
    else:
        RainfallDict[year] += rainy
        
RainfallFile.close()
RainfallYearFile = open("RAINFALLYEAR.txt", "w")
RainfallYearFile.write("Year,Rainy Days\n")
for year in RainfallDict:
    RainyDays = str(RainfallDict[year])
    year      = str(year)
    RainfallYearFile.write("{0},{1}\n".format(year, RainyDays))
RainfallYearFile.close()

## TASK 1.2

def ShowMenu():
    print("1. Query total rainy days in any year")
    print("2. Query by year the month of highest rainy days")
    print("3. -1 to Exit")

## TASK 1.3

def Query1():
    IsValid       = False                # is the year input valid?
    while IsValid == False:
        YearInput = input("Enter the year: ")
        if YearInput.isdigit():
            IsValid = True
        else:
            print("The year entered is not an integer.")
            print()

    YearInput    = int(YearInput)
    RainfallFile = open("RAINFALL.txt", "r")

    # stores number of rainy days in each year:
    # {year: number of rainy days}
    RainfallDict = {}
    RainfallFile.readline()             # exclude first line
    for line in RainfallFile:
        if line[-1] == "\n":
            line = line[:-1]
        record = line.split(",")
        year   = int(record[0][0:4])    # current year
        rainy  = int(record[1])         # number of rainy days in a month

        # if year is not in dict
        if year not in RainfallDict.keys():
            RainfallDict[year] = rainy
        else:
            RainfallDict[year] += rainy
            
    RainfallFile.close()
    if YearInput not in RainfallDict.keys():    # no data found for year
        print("Data for", YearInput, "is not available.")
    else:
        print("Number of rainy days in " + str(YearInput) + ":", RainfallDict[YearInput])
    print()

def Query2():
    IsValid       = False                # is the year input valid?
    while IsValid == False:
        YearInput = input("Enter the year: ")
        if YearInput.isdigit():
            IsValid = True
        else:
            print("The year entered is not an integer.")
            print()

    YearInput    = int(YearInput)
    RainfallFile = open("RAINFALL.txt", "r")

    MonthsDict   = { 1: "January"  ,  2: "February",  3: "March"   ,  4: "April", \
                     5: "May"      ,  6: "June"    ,  7: "July"    ,  8: "August", \
                     9: "September", 10: "October" , 11: "November", 12: "December" }

    HighestRainfall = (-1, -1)          # (rainy days, month no.)
    RainfallFile.readline()             # exclude first line
    for line in RainfallFile:
        if line[-1] == "\n":
            line = line[:-1]
        record = line.split(",")
        year   = int(record[0][0:4])    # current year
        month  = int(record[0][5:7])    # current month
        rainy  = int(record[1])         # number of rainy days in a month

        if year == YearInput:
            if rainy > HighestRainfall[0]:
                HighestRainfall = (rainy, month)
                
    RainfallFile.close()
    
    # data for that year is not available
    if HighestRainfall == (-1, -1):
        print("Data for", YearInput, "is not available.")
    else:
        rainy, month = HighestRainfall
        print("Highest number of rainy days in a month in", YearInput, "occurs in", MonthsDict[month] + ", at", rainy, "rainy days.")
    print()    

def main():
    choice = "0"
    while choice != "3":
        ShowMenu()
        choice = input("Enter your choice here: ")
        if choice == "1":
            Query1()
        elif choice == "2":
            Query2()
        elif choice == "3":
            break   # exit out of loop
        else:
            print("The option enter is invalid, please try again.")
            print()
