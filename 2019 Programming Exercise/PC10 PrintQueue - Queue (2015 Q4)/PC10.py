def ValidateUserID(ThisUserID):
    if len(ThisUserID) != 9:
        return 1
    if ThisUserID[:5] != "2015_":
        return 2
    if not ThisUserID[5:].isdigit():
        return 3
    return 0

def Task2():
    UserID = input("Enter an ID here: ")
    ValidationMessages = ["Valid User ID", "Invalid User ID - The User ID was not 9 characters", \
                          'Invalid User ID - The User ID does not start with "2015_"', \
                          'Invalid User ID - The User ID contains non-digit character']
    print(ValidationMessages[ValidateUserID(UserID)])

class PrintJob:
    # constructor function
    def __init__(self, UserID, TerminalNo, FileSize):
        self.__UserID = UserID
        self.__TerminalNo = TerminalNo
        self.__FileSize = FileSize

    # accessor functions (getters)
    def GetUserID(self):
        return self.__UserID
    
    def GetTerminalNo(self):
        return self.__TerminalNo

    def GetFileSize(self):
        return self.__FileSize

    # mutator functions (setters)
    def SetUserID(self, NewUserID):
        self.__UserID = NewUserID

    def SetTerminalNo(self, NewTerminalNo):
        self.__TerminalNo = NewTerminalNo

    def SetFileSize(self, NewFileSize):
        self.__FileSize = NewFileSize

class PrintQueue:
    def __init__(self, MaxSize = 5):
        self.__Data = [None for i in range(MaxSize)]  # initialise None
        self.__FrontPtr = 0
        self.__RearPtr = 0
        self.__CurrentSize = 0

    def IsEmpty(self):
        return (self.__CurrentSize == 0)

    def IsFull(self):
        # len(self.__Data) represents the maximum size of the queue
        return (self.__CurrentSize == len(self.__Data))

    def Insert(self, UserID, TerminalNo, FileSize):
        if self.IsFull():
            print("Print queue is full, cannot insert print job!")
        else:
            NewPrintJob = PrintJob(UserID, TerminalNo, FileSize)
            self.__CurrentSize += 1
            self.__Data[self.__RearPtr] = NewPrintJob
            
            # rear pointer points to the top element
            if self.__RearPtr == len(self.__Data) - 1:
                self.__RearPtr = 0      # set as 0 due to circular queue
            else:
                self.__RearPtr += 1     # push back rear pointer
            

    def Remove(self):
        if self.IsEmpty():
            print("Print queue is empty, no print jobs to remove!")
        else:
            self.__CurrentSize -= 1

            # if front pointer points to the top element
            if self.__FrontPtr == len(self.__Data) - 1:
                self.__FrontPtr = 0     # set as 0 due to circular queue
            else:
                self.__FrontPtr += 1    # push back front pointer
            

    def Display(self):
        print("Size of print queue: {0} out of {1} maximum".format(self.__CurrentSize, len(self.__Data)))

        # from front pointer to rear pointer
        print("Print queue (from earliest inserted to latest inserted):")
        print()
        print("-"*46)
        print("| {0:^12} | {1:^12} | {2:^12} |".format("User ID", "Terminal No.", "File Size"))
        print("-"*46)

        Current = self.__FrontPtr
        count = 0
        while count != self.__CurrentSize:
            CurrJob = self.__Data[Current]
            print("| {0:^12} | {1:^12} | {2:^12} |".format(CurrJob.GetUserID(), \
                                                           CurrJob.GetTerminalNo(), \
                                                           CurrJob.GetFileSize()))
            count += 1
            if Current == len(self.__Data) - 1:
                Current = 0
            else:
                Current += 1
            

        print("-"*46)
        print()
        
a = PrintQueue()
a.Insert(1, 2, 3)
a.Insert(4, 5, 6)
a.Insert(1, 7, 9)
a.Insert(1, 4, 3)
a.Insert(5, 2, 2)
a.Display()
