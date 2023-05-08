## TASK 4.1
class Node:
    def __init__(self, Data = "", Priority = -1, Pointer = -1):
        self.__Data     = str(Data)
        self.__Priority = int(Priority)
        self.__Pointer  = int(Pointer)

    def SetData(self, Data = ""):
        self.__Data     = str(Data)

    def GetData(self):
        return self.__Data

    def SetPriority(self, Priority = -1):
        self.__Priority = int(Priority)

    def GetPriority(self):
        return self.__Priority

    def SetPointer(self, Pointer = ""):
        self.__Pointer  = int(Pointer)
        
    def GetPointer(self):
        return self.__Pointer

class PQueue:
    def __init__(self): # Initialise()
        self.__ThisPQueue = [Node() for i in range(10)]
        for i in range(10 - 1):
            self.__ThisPQueue[i].SetPointer(i + 1)
        self.__Front    = int(-1)
        self.__Rear     = int(-1)
        self.__NextFree = int(0)

    def JoinPQueue(self, NewItem = "", Priority = -1):
        NewItem  = str(NewItem)
        Priority = int(Priority)

        NewNode  = Node(NewItem, Priority)

        # CASE 1: priority queue is full
        if self.__NextFree == -1:
            print("Cannot add to priority queue; priority queue is full!")
        else:
            temp = self.__ThisPQueue[self.__NextFree].GetPointer()
            self.__ThisPQueue[self.__NextFree] = NewNode

            # CASE 2: priority queue is empty
            if self.__Front == -1:
                self.__Front = self.__NextFree
                self.__Rear  = self.__NextFree

                # last element pointer set as -1
                self.__ThisPQueue[self.__NextFree].SetPointer(-1)
            else:
                current  = self.__Front
                previous = self.__Front
                while Priority <= self.__ThisPQueue[current].GetPriority() and current != -1:
                    previous = current
                    current  = self.__ThisPQueue[current].GetPointer()

                # CASE 3: lowest in priority
                if current == -1:
                    self.__ThisPQueue[previous].SetPointer(self.__NextFree)
                    self.__Rear = self.__NextFree

                    # last element pointer set as -1
                    self.__ThisPQueue[self.__NextFree].SetPointer(-1)

                # CASE 4: first in priority
                elif current == self.__Front:
                    self.__ThisPQueue[self.__NextFree].SetPointer(self.__Front)
                    self.__Front = self.__NextFree

                # CASE 5: anywhere else
                else:
                    self.__ThisPQueue[previous].SetPointer(self.__NextFree)
                    self.__ThisPQueue[self.__NextFree].SetPointer(current)

            self.__NextFree = temp

    def LeavePQueue(self):

        # CASE 1: priority queue is empty
        if self.__Front == -1:
            print("Priority queue is empty, cannot remove node!")
            return -1
        else:
            # CASE 2  : priority queue is not empty
            RemovedNode  = self.__Front
            self.__Front = self.__ThisPQueue[RemovedNode].GetPointer()

            # CASE 2a: only one node in priority queue
            if self.__Front == -1:
                self.__Rear = -1

            OldNextFree = self.__NextFree
            self.__NextFree = RemovedNode
            self.__ThisPQueue[RemovedNode].SetPointer(OldNextFree)
            return self.__ThisPQueue[RemovedNode].GetData()
                
    ## TASK 4.2
    def OutputPQueue(self):
        print("   Front:", self.__Front)
        print("    Rear:", self.__Rear)
        print("NextFree:", self.__NextFree)

        print("-" * 73)
        print("| {0:^10} | {1:^20} | {2:^15} | {3:^15} |".format("Index", "Data", "Priority", "Pointer"))
        print("-" * 73)

        for i in range(len(self.__ThisPQueue)):
            ThisNode = self.__ThisPQueue[i]
            ThisData = ThisNode.GetData()
            ThisPtr  = ThisNode.GetPointer()
            ThisPrio = ThisNode.GetPriority()
            print("| {0:^10} | {1:^20} | {2:^15} | {3:^15} |".format(i, ThisData, ThisPrio, ThisPtr))
            
        print("-" * 73)

## TASK 4.3
PatientQueue = PQueue()
PatientFile  = open("PATIENTS.txt", "r")
for line in PatientFile:
    if line[-1] == "\n":
        line = line[:-1]
    name, priority = line.split(",")
    name = str(name)
    priority = int(priority)
    PatientQueue.JoinPQueue(name, priority)

PatientQueue.OutputPQueue()

## TASK 4.4
MenuInput = -1
while MenuInput != 4:
    print()
    print("Patient Queue Menu")
    print()
    print("1) Add patient to PQueue")
    print("2) Remove patient from PQueue")
    print("3) Display PQueue")
    print("4) Exit program")
    print()
    MenuInput = int(input(">>> "))
    print()
    if MenuInput == 1:
        name = input("Enter the new patient's name here: ")
        priority = input("Enter the new patient's priority here: ")
        name = str(name)
        priority = int(priority)
        PatientQueue.JoinPQueue(name, priority)
        
    elif MenuInput == 2:
        PatientQueue.LeavePQueue()
        
    elif MenuInput == 3:
        PatientQueue.OutputPQueue()
                    
