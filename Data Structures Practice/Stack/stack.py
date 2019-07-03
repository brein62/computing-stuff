class Stack:    # Stack implementation using Python list
    def __init__(self, limit = 20):
        self.__Data = []
        self.__Limit = limit

    def Size(self):
        return len(self.__Data)

    def IsEmpty(self):
        return self.Size() == 0

    def IsFull(self):
        return self.Size() >= self.__Limit

    def Push(self, NewItem):
        if self.IsFull():
            print("Stack is full, cannot push!")
        elif self.IsEmpty():     # stack is empty
            self.__Data.insert(0, NewItem)
        else:
            self.__Data.insert(0, NewItem)

    def Top(self):
        return self.__Data[0]

    def __str__(self):
        output = 'Size of Stack: ' + str(self.Size()) + " in stack\n"
        output += '               ' + str(self.__Limit - self.Size()) + " remaining\n\n"
        for i in range(self.Size()):
            if self.__Data[i] != None:
                output += "| {:^15} |\n".format(self.__Data[i])
            else:
                output += "| {:^15} |\n".format("None")
                
        return output
    
    def Pop(self):
        if self.IsEmpty():       # stack is empty
            print("Stack is empty, cannot pop!")
            return -1
        else:
            return self.__Data.pop(0)

a = Stack()
a.Push(7)
a.Push(5)
a.Push(4)
a.Push(16)
a.Push(22)
a.Pop()
        
