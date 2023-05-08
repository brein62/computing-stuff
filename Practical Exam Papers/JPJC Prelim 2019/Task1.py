## TASK 1.1
VisitorsFile = open("VISITORS.txt", "r")

# dictionary storing year:number of visitors
YearsDict    = {}

VisitorsFile.read()
for line in VisitorsFile:
    if line[-1] == "\n":
        line = line[:-1]
    year, month, visitors = line.split(",")
    year     = int(year)
    visitors = int(visitors)

    # is the year not accounted for yet?
    if year not in list(YearsDict.keys()):
        YearsDict[year] = visitors
    else:
        YearsDict[year] += visitors

VisitorsFile.close()

ValidYears = False
while ValidYears == False:
    StartYear = input("Start year: ")
    EndYear   = input("  End year: ")
    if StartYear.isdigit() == False or EndYear.isdigit() == False:    # not an integer as a string
        print("The year must be an integer from 1978 to 2018.")
        continue
    else:
        StartYear = int(StartYear)
        EndYear   = int(EndYear)
        # out of range
        if StartYear < 1978 or StartYear > 2018 or EndYear < 1978 or StartYear > 2018:    
            print("The year must be in the range from 1978 to 2018.")
            continue

    if StartYear > EndYear:
        print("The end year must be greater than the start year.")
        continue
    else:
        ValidYears = True
        # print heading
        print()
        print("{0:<10}{1:<30}".format("Year", "Number of visitors"))
        for year in range(StartYear, EndYear + 1):
            print("{0:<10}{1:<30}".format(year, YearsDict[year]))

        
