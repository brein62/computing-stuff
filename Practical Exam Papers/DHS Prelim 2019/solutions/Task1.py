## TASK 1.1
def Task11():
    ScoresFile = open("IOI19.TXT", "r", encoding="utf-8")

    # store data for all countries in a 2-dimensional array:
    # [[team, golds, silvers, bronzes], ...]
    ScoresArray = []

    # exclude heading line
    ScoresFile.readline()
    for line in ScoresFile:
        if line[-1] == "\n":
            line = line[:-1]
        #Rank,First Name,Last Name,Team,Overall,Medal
        data = line.split(",")
        team  = data[3]
        medal = data[5]
        TeamIndex = -1
        for i in range(len(ScoresArray)):
            # perform a linear search to find out if
            # team is/isn't found in ScoresArray
            if ScoresArray[i][0] == team:
                TeamIndex = i
        if TeamIndex == -1:
            ScoresArray.append([team, 0, 0, 0])
            TeamIndex = len(ScoresArray) - 1

        if medal == "G":
            ScoresArray[TeamIndex][1] += 1
        elif medal == "S":
            ScoresArray[TeamIndex][2] += 1
        elif medal == "B":
            ScoresArray[TeamIndex][3] += 1

    # sort by number of golds, then number of silvers, then number of bronzes, then alphabetical order
    for i in range(len(ScoresArray)):
        for j in range(len(ScoresArray) - 1):
            if ScoresArray[j][1] < ScoresArray[j + 1][1]:
                temp = ScoresArray[j]
                ScoresArray[j] = ScoresArray[j + 1]
                ScoresArray[j + 1] = temp
            elif ScoresArray[j][1] == ScoresArray[j + 1][1]:
                if ScoresArray[j][2] < ScoresArray[j + 1][2]:
                    temp = ScoresArray[j]
                    ScoresArray[j] = ScoresArray[j + 1]
                    ScoresArray[j + 1] = temp
                elif ScoresArray[j][2] == ScoresArray[j + 1][2]:
                    if ScoresArray[j][3] < ScoresArray[j + 1][3]:
                        temp = ScoresArray[j]
                        ScoresArray[j] = ScoresArray[j + 1]
                        ScoresArray[j + 1] = temp
                    elif ScoresArray[j][3] == ScoresArray[j + 1][3]:
                        if ScoresArray[j][0] > ScoresArray[j + 1][0]:
                            temp = ScoresArray[j]
                            ScoresArray[j] = ScoresArray[j + 1]
                            ScoresArray[j + 1] = temp
                        
    print("Top 3 teams:")
    uniquemedals  = 0
    previousmedal = (0, 0, 0)
    index         = 0
    while uniquemedals < 4:
        if previousmedal != (ScoresArray[index][1], ScoresArray[index][2], ScoresArray[index][3]):
            uniquemedals += 1
            previousmedal = ScoresArray[index][1], ScoresArray[index][2], ScoresArray[index][3]
        if uniquemedals <= 3:
            medaloutput = "{0}G".format(ScoresArray[index][1])
            if ScoresArray[index][2] != 0:
                medaloutput += "{0}S".format(ScoresArray[index][2])
            if ScoresArray[index][3] != 0:
                medaloutput += "{0}B".format(ScoresArray[index][3])
            print(uniquemedals, ScoresArray[index][0], medaloutput)
            index += 1
            

    ScoresFile.close()

## TASK 1.2
def Task12():
    TeamInput = ""
    while TeamInput != "ZZZ":
        TeamInput = input("Enter team: ")
        if TeamInput != "ZZZ":
            ScoresFile = open("IOI19.TXT", "r", encoding="utf-8")

            members  = []   # array of tuples containing name and medal obtained by each member
            
            # exclude heading line
            ScoresFile.readline()
            for line in ScoresFile:
                if line[-1] == "\n":
                    line = line[:-1]
                # Rank,First Name,Last Name,Team,Overall,Medal
                data  = line.split(",")
                team  = data[3]
                name  = data[1] + " " + data[2]
                medal = data[5]
                if team == TeamInput:
                    members.append((name, medal))

            for member in members:
                print("{0:<30}{1}".format(member[0], member[1]))
            print()
                    
            ScoresFile.close()
        else:
            print("Bye")

