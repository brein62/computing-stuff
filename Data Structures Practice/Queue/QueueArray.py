class Queue:
    def __init__(self, size = 30):
        self.__data = [None for i in range(size)]
        self.__size = 0             # total size in queue
        self.__front = 0            # front pointer
        self.__rear = 0             # rear pointer

    def IsEmpty(self):
        return (self.__size == 0)

    def IsFull(self):
        return (self.__size == len(self.__data))
    
    def InsertItem(self, NewData):
        if self.IsFull():
            print("Queue Overflow! - while inserting '{0}'".format(NewData))
        else:
            self.__data[self.__rear] = NewData
            if self.__rear == (len(self.__data) - 1):
                self.__rear = 0
            else:
                self.__rear += 1
            self.__size += 1

    def DeleteItem(self):
        if self.IsEmpty():
            print("Queue Underflow! - item is deleted while queue is empty")
        else:
            DeletedItem = self.__data[self.__front]
            self.__data[self.__front] = None
            self.__size -= 1
            if self.__front == (len(self.__data) - 1):
                self.__front = 0
            else:
                self.__front += 1
            return DeletedItem

    def __str__(self):
        output = ""
        for i in range(len(self.__data) - 1, -1, -1):            # from the back
            if self.__data[i] == None:
                output += ("|{0:^10}|{1:^40}|".format(i, "None"))
            else:
                output += ("|{0:^10}|{1:^40}|".format(i, self.__data[i]))
            if (self.__front == self.__rear and self.__front == i):
                output += " <-- FP, RP\n"
            elif self.__front == i:
                output += " <-- FP\n"
            elif self.__rear == i:
                output += " <-- RP\n"
            else:
                output += "\n"
        return output

    def DisplayInOrder(self):
        i = self.__front
        if self.__rear == 0:
            for i in range(self.__front, len(self.__data) - 1):
                print(self.__data[i], end=" -> ")
            print(self.__data[-1])
        elif self.__front >= self.__rear and not self.IsEmpty():
            while i < len(self.__data):
                print(self.__data[i], end=" -> ")
                i += 1
            i = 0
            while i < (self.__rear - 1):
                print(self.__data[i], end=" -> ")
                i += 1
            print(self.__data[i])
        else:
            for i in range(self.__front, self.__rear - 1):
                print(self.__data[i], end=" -> ")
            print(self.__data[self.__rear - 1])
                

def main():
    a = Queue(4)
    a.InsertItem("34")
    a.InsertItem("1233")
    a.InsertItem("hello")
    a.InsertItem("world")
    a.DeleteItem()
    a.DisplayInOrder()
    print(a)
