class BookRec:
    def __init__(self, BookID, Title, Pointer):
        self.__BookID = BookID
        self.__Title = Title
        self.__Pointer = Pointer
    def GetBookID(self):
        return self.__BookID
    def GetTitle(self):
        return self.__Title
    def GetPointer(self):
        return self.__Pointer
    def SetBookID(self, BookID):
        self.__BookID = BookID
    def SetTitle(self, Title):
        self.__Title = Title
    def SetPointer(self, Pointer):
        self.__Pointer = Pointer

class LinkedList:
    def __init__(self):
        self.__Start = None         # null
    
    def IsEmpty(self):
        return (self.__Start == None)

    def DisplayLinkedList(self):
        curr = self.__Start         # current node
        while curr != None:
            print("{0} -> ".format(curr.GetBookID()))
            curr = curr.GetPointer()

    def AddNode(self, BookID, Title):
        NewNode = BookRec(BookID, Title, None)
        if self.IsEmpty():
            self.__Start = NewNode
        else:
            curr = self.__Start
            while curr.GetPointer() != None:
                curr = curr.GetPointer()
            curr.SetPointer(NewNode)

    def SearchNode(self, BookID):
        curr = self.__Start
        while curr != None and curr.GetBookID() != BookID:
            curr = curr.GetPointer()
        if curr == None:
            return False
        else:
            return True
        # return (curr == None)

    def DeleteNode(self, BookID):
        if self.SearchNode(BookID):
            prev = self.__Start
            curr = self.__Start
            while curr != None and curr.GetBookID() != BookID:
                prev = curr
                curr = curr.GetPointer()
            prev.SetPointer(curr.GetPointer())

    
    
        

    
