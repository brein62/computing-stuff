class ListNode:
    def __init__(self, Name = "", Pointer = -1):
        self.__Name = Name
        self.__Pointer = Pointer
    def GetName(self):
        return self.__Name
    def SetName(self, NewName):
        self.__Name = NewName
    def GetPointer(self):
        return self.__Pointer
    def SetPointer(self, NewPointer):
        self.__Pointer = NewPointer

class LinkedList:
    def __init__(self, Size = 20):
        self.__Node = [ListNode() for i in range(Size)]
        for i in range(Size - 1):
            self.__Node[i].SetPointer(i + 1)
        self.__Start = -1
        self.__NextFree = 0

    def Display(self):
        print("{:^10} | {:^20} | {:^10}".format("Node", "Name", "Pointer"))
        print("-"*46)
        for i in range(len(self.__Node)):
            print("{:^10} | {:^20} | {:^10}".format(i, self.__Node[i].GetName(), self.__Node[i].GetPointer()))
        print()
        print("Start =", str(self.__Start))
        print("NextFree =", str(self.__NextFree))

    def IsEmpty(self):
        return self.__Start == -1

    def IsFull(self):
        return self.__NextFree == -1

    def Insert(self, NewName):
        if self.__NextFree == -1:                           #no free nodes
            print("No space to insert.")
            return
        self.__Node[self.__NextFree].SetName(NewName)       #store in next free node
        if self.__Start == -1:                              #insert into empty list
            HoldFree = self.__Node[self.__NextFree].GetPointer()
            self.__Node[self.__NextFree].SetPointer(-1)
            self.__Start = self.__NextFree
            self.__NextFree = HoldFree
        else:
            if NewName < self.__Node[self.__Start].GetName():   #as first node of list
                HoldFree = self.__Node[self.__NextFree].GetPointer()
                self.__Node[self.__NextFree].SetPointer(self.__Start)
                self.__Start = self.__NextFree
                self.__NextFree = HoldFree   
            else:
                Previous = self.__Start
                Current = self.__Start
                while NewName > self.__Node[Current].GetName() and self.__Node[Current].GetPointer() != -1:
                    #search position to insert node
                    Previous = Current
                    Current = self.__Node[Current].GetPointer()
                if NewName > self.__Node[Current].GetName() and self.__Node[Current].GetPointer() == -1:
                    #insert at last node of list
                    HoldFree = self.__Node[self.__NextFree].GetPointer()
                    self.__Node[Current].SetPointer(self.__NextFree)
                    self.__Node[self.__NextFree].SetPointer(-1)
                    self.__NextFree = HoldFree
                else:   #insert in between nodes
                    HoldFree = self.__Node[self.__NextFree].GetPointer()
                    self.__Node[Previous].SetPointer(self.__NextFree)
                    self.__Node[self.__NextFree].SetPointer(Current)
                    self.__NextFree = HoldFree

    def Query(self):
        CountryInput = input("Enter a country name: ")
        Previous = self.__Start
        Current = self.__Start
        while CountryInput > self.__Node[Current].GetName() and Current != -1:
            #traverse linked list to find node
            Previous = Current
            Current = self.__Node[Current].GetPointer()
        if CountryInput == self.__Node[Current].GetName():  #country is found
            print("{} is found in the linked list, at position {}.".format(CountryInput, Current))
        else:
            print("{} is not found in the linked list.".format(CountryInput))
            

CountryFile = open("COUNTRIES.txt", "r")
CountryList = LinkedList()          #new linked list
for Country in CountryFile:
    if Country[-1] == "\n":         #not the last line
        CountryList.Insert(Country[:-1])
    else:                           #the last line
        CountryList.Insert(Country)
CountryFile.close()
CountryList.Display()
CountryList.Query()
CountryList.Query()
