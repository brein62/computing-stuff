## TASK 3.1
def GetALFromScore(score):
    score = int(score)
    if score >= 90:
        return 1
    elif score >= 85:
        return 2
    elif score >= 80:
        return 3
    elif score >= 75:
        return 4
    elif score >= 65:
        return 5
    elif score >= 45:
        return 6
    elif score >= 20:
        return 7
    else:
        return 8

PSLEFile = open("PSLE21.txt", "r")
PSLEDict = {}

# PSLEDict
# { StudentID : PSLEScore, Citizenship, Choice1, Choice2, Choice3 }
for record in PSLEFile:
    if record[-1] == "\n":
        record = record[:-1]
    StudentID, ELMark, MAMark, SCMark, MTMark, Citizenship, Choice1, Choice2, Choice3 = record.split(",")
    PSLEScore = GetALFromScore(int(ELMark)) + GetALFromScore(int(MAMark)) +\
                GetALFromScore(int(SCMark)) + GetALFromScore(int(MTMark))
    PSLEDict[StudentID] = (PSLEScore, Citizenship, Choice1, Choice2, Choice3)

PSLEDictKeys = list(PSLEDict.keys())
for i in range(10):
    print(PSLEDictKeys[i] + ":", PSLEDict[PSLEDictKeys[i]])
    
PSLEFile.close()

## TASK 3.2 (160 lines for 16 marks is not acceptable)
class Node:
    def __init__(self, Pointer, StudentID = "", PSLEScore = 0, Citizenship = "", Choice1 = "", Choice2 = "", Choice3 = ""):
        self.__PSLEScore   = int(PSLEScore)
        self.__StudentID   = str(StudentID)
        self.__Citizenship = str(Citizenship)
        self.__Choice1     = str(Choice1)
        self.__Choice2     = str(Choice2)
        self.__Choice3     = str(Choice3)
        self.__Pointer     = Pointer

    def SetPSLEScore(self, PSLEScore = 0):
        self.__PSLEScore   = int(PSLEScore)
    def SetStudentID(self, StudentID = ""):
        self.__StudentID   = str(StudentID)
    def SetCitizenship(self, Citizenship = ""):
        self.__Citizenship = str(Citizenship)
    def SetChoice1(self, Choice1 = ""):
        self.__Choice1     = str(Choice1)
    def SetChoice2(self, Choice2 = ""):
        self.__Choice2     = str(Choice2)
    def SetChoice3(self, Choice3 = ""):
        self.__Choice3     = str(Choice3)
    def SetPointer(self, Pointer):
        self.__Pointer     = Pointer

    def GetPSLEScore(self):
        return self.__PSLEScore
    def GetStudentID(self):
        return self.__StudentID
    def GetCitizenship(self):
        return self.__Citizenship
    def GetChoice1(self):
        return self.__Choice1
    def GetChoice2(self):
        return self.__Choice2
    def GetChoice3(self):
        return self.__Choice3
    def GetPointer(self):
        return self.__Pointer

# dynamic linked list implementation
class LinkedList:
    
    # MaxSize depends on school enrolment
    def __init__(self, MaxSize = 150):
        self.__NextFree = 0
        self.__MaxSize  = MaxSize
        self.__Start = None
        self.__CurrentSize = 0

    def IsEmpty(self):
        return self.__Start == None

    def IsFull(self):
        return self.__CurrentSize == self.__MaxSize

    def AddNode(self, StudentID = "", PSLEScore = 0, Citizenship = "", Choice1 = "", Choice2 = "", Choice3 = ""):
        NewNode = Node(None, StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)
        if self.IsEmpty():
            self.__Start = NewNode
            self.__CurrentSize += 1
            return True
        elif self.IsFull():
            return False   # cannot add to linked list
        else:
            previous = self.__Start
            current  = self.__Start
            while current != None:
                previous = current
                current  = current.GetPointer()
            previous.SetPointer(NewNode)
            self.__CurrentSize += 1
            return True

    def RemoveNode(self, StudentID = ""):
        previous = self.__Start
        current  = self.__Start
        while current != None and current.GetStudentID() != StudentID:
            previous = current
            current  = current.GetPointer()

        if current == None:
            print("Student not found, cannot remove from linked list!")
        else:
            previous.SetPointer(current.GetPointer())
            self.__CurrentSize -= 1

    def Display(self):
        print("{0:<14}{1:<20}{2:<20}{3:<14}{4:<14}{5:<14}".format("Student ID", "PSLE Score", "Citizenship", "First Choice", "Second Choice", "Third Choice"))
        current = self.__Start
        while current != None:
            print("{0:<14}{1:<20}{2:<20}{3:<14}{4:<14}{5:<14}".format(current.GetStudentID(), current.GetPSLEScore(), current.GetCitizenship(),\
                                                                      current.GetChoice1()  , current.GetChoice2()  , current.GetChoice3()    ))
                  
            current = current.GetPointer()

def Priority(Citizenship):
    PriorityDict = {"SC": 3, "PR": 2, "IS": 1}
    return PriorityDict[Citizenship]

def AssignSchools():
    SchoolA = LinkedList(120)
    SchoolB = LinkedList(150)
    SchoolC = LinkedList(80)
    SchoolD = LinkedList(400)
    SortedStudentID = list(PSLEDict.keys())
    # bubble sort to sort the Student ID by PSLE score, then by priority
    for i in range(len(SortedStudentID)):
        for j in range(len(SortedStudentID) - 1):
            if PSLEDict[SortedStudentID[j]][0] > PSLEDict[SortedStudentID[j + 1]][0]:
                temp = SortedStudentID[j]
                SortedStudentID[j] = SortedStudentID[j + 1]
                SortedStudentID[j + 1] = temp
            elif PSLEDict[SortedStudentID[j]][0] == PSLEDict[SortedStudentID[j + 1]][0]:
                if Priority(PSLEDict[SortedStudentID[j]][1]) < Priority(PSLEDict[SortedStudentID[j + 1]][1]):
                    temp = SortedStudentID[j]
                    SortedStudentID[j] = SortedStudentID[j + 1]
                    SortedStudentID[j + 1] = temp

    SecondTry = []  # students who need to go to the second choice
    for StudentID in SortedStudentID:
        PSLEScore, Citizenship, Choice1, Choice2, Choice3 = PSLEDict[StudentID]
        if Choice1 == "SCHOOLA":
            Accepted = SchoolA.AddNode(StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)
        elif Choice1 == "SCHOOLB":
            Accepted = SchoolB.AddNode(StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)
        elif Choice1 == "SCHOOLC":
            Accepted = SchoolC.AddNode(StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)
            
        if Accepted == False:
            SecondTry.append(StudentID)

    ThirdTry = []  # students who need to go to the third choice
    for StudentID in SecondTry:
        PSLEScore, Citizenship, Choice1, Choice2, Choice3 = PSLEDict[StudentID]
        if Choice2 == "SCHOOLA":
            Accepted = SchoolA.AddNode(StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)
        elif Choice2 == "SCHOOLB":
            Accepted = SchoolB.AddNode(StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)
        elif Choice2 == "SCHOOLC":
            Accepted = SchoolC.AddNode(StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)
            
        if Accepted == False:
            ThirdTry.append(StudentID)

    for StudentID in ThirdTry:
        PSLEScore, Citizenship, Choice1, Choice2, Choice3 = PSLEDict[StudentID]
        if Choice3 == "SCHOOLA":
            Accepted = SchoolA.AddNode(StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)
        elif Choice3 == "SCHOOLB":
            Accepted = SchoolB.AddNode(StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)
        elif Choice3 == "SCHOOLC":
            Accepted = SchoolC.AddNode(StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)
            
        if Accepted == False:
            # no other choices
            SchoolD.AddNode(StudentID, PSLEScore, Citizenship, Choice1, Choice2, Choice3)

    print("School A:")
    SchoolA.Display()
    print()
    print("School B:")
    SchoolB.Display()
    print()
    print("School C:")
    SchoolC.Display()
    print()
    print("School D")
    SchoolD.Display()

AssignSchools()

## TASK 3.3
P351Record = (PSLEDict["P351"][0], "SC", PSLEDict["P351"][2], PSLEDict["P351"][3], PSLEDict["P351"][4])
P365Record = (PSLEDict["P365"][0], "SC", PSLEDict["P365"][2], PSLEDict["P365"][3], PSLEDict["P365"][4])
PSLEDict["P351"] = P351Record
PSLEDict["P365"] = P365Record
AssignSchools()

## TASK 3.4


