########    TASK 1    ########

def CreateUpdateFile():
    ResultsFile = open("RESULTS.txt", "r")
    NewFile     = open("NEWFILE.txt", "w")
    line = ResultsFile.readline()
    if line[-1] == "\n":
        line = line[:-1]
    MatchInfo = line.split(" ")
    Team1  = MatchInfo[0]
    Score1 = MatchInfo[1]
    Team2  = MatchInfo[2]
    Score2 = MatchInfo[3]
    if Score1 < Score2:         # Team1 loses
        NewFile.write("{0},{1},{2},{3}\n".format(Team1, "L", Score1, Score2))
        NewFile.write("{0},{1},{2},{3}\n".format(Team2, "W", Score2, Score1))
    elif Score1 == Score2:      # drawn game
        NewFile.write("{0},{1},{2},{3}\n".format(Team1, "D", Score1, Score2))
        NewFile.write("{0},{1},{2},{3}\n".format(Team2, "D", Score2, Score1))
    else:                       # Team1 wins
        NewFile.write("{0},{1},{2},{3}\n".format(Team1, "W", Score1, Score2))
        NewFile.write("{0},{1},{2},{3}\n".format(Team2, "L", Score2, Score1))

########   TASK 2   #########

def CreateUpdateFileAmended():
    ResultsFile = open("RESULTS.txt", "r")
    NewFile     = open("NEWFILE.txt", "w")
    for line in ResultsFile:
        if line[-1] == "\n":
            line = line[:-1]
        MatchInfo = line.split(" ")
        Team1  = MatchInfo[0]
        Score1 = MatchInfo[1]
        Team2  = MatchInfo[2]
        Score2 = MatchInfo[3]
        if Score1 < Score2:         # Team1 loses
            NewFile.write("{0},{1},{2},{3}\n".format(Team1, "L", Score1, Score2))
            NewFile.write("{0},{1},{2},{3}\n".format(Team2, "W", Score2, Score1))
        elif Score1 == Score2:      # drawn game
            NewFile.write("{0},{1},{2},{3}\n".format(Team1, "D", Score1, Score2))
            NewFile.write("{0},{1},{2},{3}\n".format(Team2, "D", Score2, Score1))
        else:                       # Team1 wins
            NewFile.write("{0},{1},{2},{3}\n".format(Team1, "W", Score1, Score2))
            NewFile.write("{0},{1},{2},{3}\n".format(Team2, "L", Score2, Score1))
            
    
    ResultsFile.close()
    NewFile.close()

########   TASK 3   #########

def ComputeTeamStat(TeamName):
    NewFile      = open("NEWFILE.txt", "r")
    Played       = 0
    Won          = 0
    Drawn        = 0
    Lost         = 0
    TotalFor     = 0                    # total no. of goals for
    TotalAgainst = 0                    # total no. of goals against
    GoalDiff     = 0
    Points       = 0
    for line in NewFile:
        if line[-1] == "\n":
            line = line[:-1]
        MatchInfo = line.split(",")
        Team         = MatchInfo[0]
        Result       = MatchInfo[1]
        GoalsFor     = MatchInfo[2]     # goals for in each match
        GoalsAgainst = MatchInfo[3]     # goals against in each match
        if Team == TeamName:
            Played += 1
            if Result == "W":           # won
                Won += 1
            elif Result == "D":         # drawn
                Drawn += 1
            else:                       # lost
                Lost += 1

            TotalFor += int(GoalsFor)
            TotalAgainst += int(GoalsAgainst)

    GoalDiff = TotalFor - TotalAgainst
    Points = Won * 3 + Drawn * 1 + Lost * 0
    print("{0:<15}{1:<5}{2:<5}{3:<5}{4:<5}{5:<5}{6:<5}{7:<5}{8}".format(TeamName, Played, Won, Drawn, Lost, TotalFor, TotalAgainst, GoalDiff, Points))
    NewFile.close()

    return (Played, Won, Drawn, Lost, TotalFor, TotalAgainst, GoalDiff, Points)


########   TASK 4   #########
    
def GenerateTable():

    # print heading
    print("{0:<15}{1:<5}{2:<5}{3:<5}{4:<5}{5:<5}{6:<5}{7:<5}{8}".format("Team", "P", "W", "D", "L", "GF", "GA", "GD", "Points"))
    print("-" * 56)
    TeamsFile = open("TEAMS.txt", "r")
    TeamsList = []
    for line in TeamsFile:
        if line[-1] == "\n":
            line = line[:-1]
        TeamsList += [line]

    for team in TeamsList:
        ComputeTeamStat(team)
        
    TeamsFile.close()


########   TASK 5   #########

# ComputeTeamStat(TeamName) except without printing
def ComputeTeamStat2(TeamName):
    NewFile      = open("NEWFILE.txt", "r")
    Played       = 0
    Won          = 0
    Drawn        = 0
    Lost         = 0
    TotalFor     = 0                    # total no. of goals for
    TotalAgainst = 0                    # total no. of goals against
    GoalDiff     = 0
    Points       = 0
    for line in NewFile:
        if line[-1] == "\n":
            line = line[:-1]
        MatchInfo = line.split(",")
        Team         = MatchInfo[0]
        Result       = MatchInfo[1]
        GoalsFor     = MatchInfo[2]     # goals for in each match
        GoalsAgainst = MatchInfo[3]     # goals against in each match
        if Team == TeamName:
            Played += 1
            if Result == "W":           # won
                Won += 1
            elif Result == "D":         # drawn
                Drawn += 1
            else:                       # lost
                Lost += 1

            TotalFor += int(GoalsFor)
            TotalAgainst += int(GoalsAgainst)

    GoalDiff = TotalFor - TotalAgainst
    Points = Won * 3 + Drawn * 1 + Lost * 0
    NewFile.close()

    return (Points, GoalDiff, TeamName, Played, Won, Drawn, Lost, TotalFor, TotalAgainst)

# StatTuple: (Points, GoalDiff, TeamName, Played, Won, Drawn, Lost, TotalFor, TotalAgainst)
def PrintTeamStat(StatTuple):
    Points       = StatTuple[0]
    GoalDiff     = StatTuple[1]
    TeamName     = StatTuple[2]
    Played       = StatTuple[3]
    Won          = StatTuple[4]
    Drawn        = StatTuple[5]
    Lost         = StatTuple[6]
    TotalFor     = StatTuple[7]
    TotalAgainst = StatTuple[8]
    print("{0:<15}{1:<5}{2:<5}{3:<5}{4:<5}{5:<5}{6:<5}{7:<5}{8}".format(TeamName, Played, Won, Drawn, Lost, TotalFor, TotalAgainst, GoalDiff, Points))

def GenerateTableAmended():

    # print heading
    print("{0:<15}{1:<5}{2:<5}{3:<5}{4:<5}{5:<5}{6:<5}{7:<5}{8}".format("Team", "P", "W", "D", "L", "GF", "GA", "GD", "Points"))
    print("-" * 56)
    TeamsFile = open("TEAMS.txt", "r")
    TeamStatsList = []
    for line in TeamsFile:
        if line[-1] == "\n":
            team = line[:-1]
        TeamStatsList.append(ComputeTeamStat2(team))

    # perform a bubble sort
    for i in range(len(TeamStatsList)):
        for j in range(len(TeamStatsList)):
            if TeamStatsList[i] > TeamStatsList[j]:
                # swap
                TeamStatsList[i], TeamStatsList[j] = TeamStatsList[j], TeamStatsList[i]

    for TeamStat in TeamStatsList:
        PrintTeamStat(TeamStat)
        
    TeamsFile.close()
