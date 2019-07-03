class ListNode:
    def __init__(self,Name,Pointer):
        self.__Name = Name
        self.__Pointer = Pointer
    def Insert(self,newvalue):
        if self.IsFull():
            print("No space to insert")
            return
        self.__Node[self.__NextFree].setName(newvalue)
        if start = -1:
            holdfree = self.__Node[self.__NextFree].getPointer()
            self.__Node[self.__NextFree].setPointer(-1)
            self.__Start = self.__NextFree
            self.__NextFree = holdfree
        else:
            if newvalue < self.__Node[self.__Start].getName():
                holdfree = self.__Node[self.__NextFree].getPointer()
                self.__Node[self.__NextFree].setPointer(self.__Start)
                    
