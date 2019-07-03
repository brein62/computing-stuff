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
    def __init__(self, UserID, Terminal, FileSize):
        self.__UserID = UserID
        self.__Terminal = Terminal
        self.__FileSize = FileSize

    def GetUserID(self):
        return self.__UserID
    def GetTerminal(self):
        return self.__Terminal
    def GetFileSize(self):
        return self.__FileSize
    def SetUserID(self, NewUserID):
        self.__UserID = NewUserID
    def SetTerminal(self, NewTerminal):
        self.__Terminal = NewTerminal
    def SetFileSize(self, NewFileSize):
        self.__FileSize = FileSize

class PrintQueue:
    def __init__(self, limit = 5):
        self.__front = 0
        self.__rear = 0
        self.__limit = limit
        self.__size = 0
        self.__data = [PrintJob(None, None, None) for i in range(limit)]
        
    def IsEmpty(self):
        return self.__size == 0

    def IsFull(self):
        return self.__limit == 0

    def InsertPrintJob(self, UserID, Terminal, FileSize):
        if self.IsFull():
            print("Print queue is full, cannot insert print job.")
        else:
            NewPrintJob = PrintJob(UserID, Terminal, FileSize)
            self.__data[self.__rear] = NewPrintJob
            if (self.__rear == self.__limit - 1):
                self.__rear = 0
            else:
                self.__rear += 1
            self.__size += 1

    def RemovePrintJob(self):
        if self.IsEmpty():
            print("No print jobs in print queue, cannot remove print job.")
        else:
            RemovedPrintJob = self.__data[self.__front]
            if (self.__front == self.__limit - 1):
                self.__front = 0
            else:
                self.__front += 1
            self.__size -= 1
            return RemovedPrintJob

    def __str__(self):          # displays the print queue
        index = self.__front
        output = "|{0:^20}|{1:^20}|{2:^20}|\n".format("User ID", "Terminal Number", "File Size")
        if (self.IsEmpty()):
            return output
        elif (self.__rear == 0):
            while index < self.__limit:
                output += "|{0:^20}|{1:^20}|{2:^20}|".format(self.__data[index].GetUserID(), \
                                                             self.__data[index].GetTerminal(), \
                                                             self.__data[index].GetFileSize())
                index += 1
            return output
        elif (self.__front < self.__rear):
            while index < self.__rear:
                output += "|{0:^20}|{1:^20}|{2:^20}|".format(self.__data[index].GetUserID(), \
                                                             self.__data[index].GetTerminal(), \
                                                             self.__data[index].GetFileSize())
                index += 1
            return output
        else:
            while index < self.__limit:
                output += "|{0:^20}|{1:^20}|{2:^20}|".format(self.__data[index].GetUserID(), \
                                                             self.__data[index].GetTerminal(), \
                                                             self.__data[index].GetFileSize())
                index += 1
            index = 0
            while index < self.__rear:
                output += "|{0:^20}|{1:^20}|{2:^20}|".format(self.__data[index].GetUserID(), \
                                                             self.__data[index].GetTerminal(), \
                                                             self.__data[index].GetFileSize())
                index += 1
            return output
            
        
            
            
    
