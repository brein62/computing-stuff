class ListNode():
    def __init__(self, Name = "", Pointer = -1): #initialising the node
        self.__Name = Name
        self.__Pointer = Pointer

    def getPointer(self):
        return self.__Pointer
    def setPointer(self, newPointer):
        self.__Pointer = newPointer
    def getName(self):
        return self.__Name
    def setName(self, newName):
        self.__Name = newName

class LinkedList():
    def __init__(self, size = 20): #initialising the linked list
        self.__Node = [ListNode() for i in range(size)]
        for i in range(size - 1):
            self.__Node[i].setPointer(i + 1)
        self.__StartPtr = -1
        self.__NextFreePtr = 0

    def DisplayList(self):
        print("{0:^10} | {1:^20} | {2:^10}".format("Node", "Country Name", "Pointer"))
        print("-"*45)       #separate heading from contents
        for i in range(len(self.__Node)):
            print("{0:^10} | {1:^20} | {2:^10}".format(i, self.__Node[i].getName(), self.__Node[i].getPointer()))
        print()
        print("Value of StartPtr: {0}".format(self.__StartPtr))
        print("Value of NextFreePtr: {0}".format(self.__NextFreePtr))

    def IsEmpty(self):
        if self.__StartPtr == -1 and self.__NextFreePtr == 0:
            return True
        else:
            return False

    def IsFull(self):
        if self.__NextFreePtr == -1:
            return True
        else:
            return False

    def InsertNode(self, NewItem):
        if self.IsFull() == True:
            print("Array is full. Cannot insert node!")
        else:                                       #array not full
            #find insertion point
            PreviousPtr = self.__StartPtr
            CurrentPtr = self.__StartPtr
            while (CurrentPtr != -1) and (self.__Node[CurrentPtr].getName() < NewItem):
                PreviousPtr = CurrentPtr
                CurrentPtr = self.__Node[CurrentPtr].getPointer()
            
            if (self.__Node[CurrentPtr].getName() == NewItem):
                print("Cannot insert repeated entries!")
            else:                       
                self.__Node[self.__NextFreePtr].setName(NewItem)
                NewNodePtr = self.__NextFreePtr
                self.__NextFreePtr = self.__Node[self.__NextFreePtr].getPointer()
                if CurrentPtr == self.__StartPtr:      #insert new node at start of list
                    self.__Node[NewNodePtr].setPointer(self.__StartPtr)
                    self.__StartPtr = NewNodePtr
                else:                                   #in between PreviousPtr and CurrentPtr
                    self.__Node[NewNodePtr].setPointer(self.__Node[PreviousPtr].getPointer())
                    self.__Node[PreviousPtr].setPointer(NewNodePtr)

    def DeleteNode(self):
        DeletedItem = input("Enter a country name to delete: ")
        if self.IsEmpty():                          #empty linked list
            print("Linked list is empty.")
            return
        PreviousPtr = self.__StartPtr
        CurrentPtr = self.__StartPtr
        while CurrentPtr != -1 and self.__Node[CurrentPtr].getName() != DeletedItem:
            PreviousPtr = CurrentPtr
            CurrentPtr = self.__Node[CurrentPtr].getPointer()
        if CurrentPtr == -1:                        #country name not found
            print("Country name is not found.")
            return
        if CurrentPtr == self.__StartPtr:           #deleting the first one
            self.__StartPtr = self.__Node[CurrentPtr].getPointer()
            self.__Node[CurrentPtr].setPointer(self.__NextFreePtr)
            self.__NextFreePtr = CurrentPtr
        else:                                       #deleting anywhere else
            self.__Node[PreviousPtr].setPointer(self.__Node[CurrentPtr].getPointer())
            self.__Node[CurrentPtr].setPointer(self.__NextFreePtr)
            self.__NextFreePtr = CurrentPtr         #makes the next free pointer the current pointer

    def OutputAllNodes(self):
        print("{0:^10} | {1:^20} | {2:^10}".format("Node", "Country Name", "Pointer"))
        print("-"*45)       #separate heading from contents
        PreviousPtr = self.__StartPtr
        CurrentPtr = self.__StartPtr
        while CurrentPtr != -1:
            PreviousPtr = CurrentPtr
            CurrentPtr = self.__Node[CurrentPtr].getPointer()
            print("{:^10} | {:^20} | {:^10}".format(PreviousPtr, self.__Node[PreviousPtr].getName(), CurrentPtr))
        
def main():
    file = open("COUNTRY.txt", "r")
    a = LinkedList()
    for line in file:
        a.InsertNode(line[:-1])
    a.DisplayList()
    a.OutputAllNodes()
    a.DeleteNode()
    a.DeleteNode()
    a.DeleteNode()
    a.DisplayList()
    a.OutputAllNodes()

main()
