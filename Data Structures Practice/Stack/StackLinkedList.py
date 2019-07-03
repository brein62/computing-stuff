class ListNode:
    def __init__(self, Data, Pointer):
        self.__Data = Data
        self.__Pointer = Pointer

    def SetData(self, NewData):
        self.__Data = NewData

    def SetPointer(self, NewPointer):
        self.__Pointer = NewPointer

    def GetData(self):
        return self.__Data

    def GetPointer(self):
        return self.__Pointer

class Stack:
    def __init__(self):
        self.__Start = None
        self.__Size = 0

    def IsEmpty(self):
        return (self.__Start == None)

    def __str__(self):
        output = ""
        if self.IsEmpty():
            output = "Stack is empty."
        else:
            output = "Number of elements in stack: " + str(self.__Size) + "\n"
            output += "-" * 42 + "\n"
            output += "|{0:^40}|\n".format("STACK")
            output += "-" * 42 + "\n"
            curr = self.__Start
            while curr != None:
                output += "|{0:^40}|\n".format(curr.GetData())
                curr = curr.GetPointer()
            output += "-" * 42 + "\n"

        return output

    def Push(self, Data):                                   # add to front
        NewNode = ListNode(Data, self.__Start)              # self.__Start: node after this new node
        self.__Start = NewNode
        self.__Size += 1

    def Pop(self):                                          # remove from front
        if self.IsEmpty():
            print("Stack is empty, cannot pop.")
        else:
            self.__Start = self.__Start.GetPointer()
            self.__Size -= 1

    def Top(self):
        if self.IsEmpty():
            return None
        else:
            return self.__Start.GetData()

    def Size(self):
        return self.__Size
        
a = Stack()
a.Push(10)
a.Push(69)
a.Push(3)
a.Push(133)
a.Pop()
a.Top()

print(a)
