
# returns "Yes" if within normal range, "No" otherwise
def WithinNormalRange(Age, Height):
    Age = int(Age)
    Height = int(Height)
    Minimum = 5.3 * Age + 71
    Maximum = 6.2 * Age + 87
    if Height < Minimum or Height > Maximum:
        return "No"
    else:
        return "Yes"

def Task11():
    HeightData = open("HEIGHTDATA.txt", "r")
    HeightList = []
    for line in HeightData:
        if line[-1] == "\n":
            line = line[:-1]
        Name, Age, Height = line.split(",")
        Age = int(Age)
        Height = int(Height)
        InRange = WithinNormalRange(Age, Height)
        HeightList.append((Name, Age, Height, InRange))

    # heading
    print("{0:<15}{1:<15}{2:<15}{3:<25}".format("Name", "Age", "Height", "Within normal range"))
    for Record in HeightList:
        Name, Age, Height, InRange = Record
        print("{0:<15}{1:<15}{2:<15}{3:<25}".format(Name, Age, Height, InRange))

# returns new fixed Height if fixes are needed, otherwise no processing is done.
# if there are 0 or more than 1 fix is needed, returns "Re-enter data".
def FixHeight(Age, Height):
    # all entered heights are 3 digits.
    # 6 possibilities: abc, acb, bac, bca, cab, cba
    Heights  = []
    Height   = str(Height)
    Heights.append(Height[0] + Height[1] + Height[2])   # abc
    Heights.append(Height[0] + Height[2] + Height[1])   # acb
    Heights.append(Height[1] + Height[0] + Height[2])   # bac
    Heights.append(Height[1] + Height[2] + Height[0])   # bca
    Heights.append(Height[2] + Height[0] + Height[1])   # cab
    Heights.append(Height[2] + Height[1] + Height[0])   # cba
    
    ValidCount = 0
    Output     = ""
    for ChangedHeight in Heights:
        ChangedHeight = int(ChangedHeight)
        if WithinNormalRange(Age, ChangedHeight) == "Yes":
            if ChangedHeight != Output:         # prevent instances where changed height is the same as another
                if ValidCount == 0:
                    Output = ChangedHeight
                else:
                    Output = "Re-enter data"
                ValidCount += 1
    return Output

def Task12():
    HeightData = open("HEIGHTDATA.txt", "r")
    HeightList = []
    for line in HeightData:
        if line[-1] == "\n":
            line = line[:-1]
        Name, Age, Height = line.split(",")
        Age = int(Age)
        Height = int(Height)
        InRange = WithinNormalRange(Age, Height)
        HeightList.append((Name, Age, Height, InRange))

    # heading
    print("{0:<15}{1:<15}{2:<15}{3:<25}".format("Name", "Age", "Height", "Corrected Height"))
    for Record in HeightList:
        Name, Age, Height, InRange = Record
        if InRange == "No":
            CorrectedHeight = FixHeight(Age, Height)
            print("{0:<15}{1:<15}{2:<15}{3:<25}".format(Name, Age, Height, CorrectedHeight))
            
        # if data is within range, do not print anything
    
