class ListNode:
    def __init__(self, data = "", pointer= -1):
        self.__DataValue = data
        self.__PointerValue = pointer

    def getData(self):
        return self.__DataValue

    def getPointer(self):
        return self.__PointerValue

    def setData(self, newdata):
        self.__DataValue = newdata

    def setPointer(self, newpointer):
        self.__PointerValue = newpointer

class LinkedList:
    def __init__(self, size = 30):                          # Initialise()
        self.__Node = [ListNode() for i in range(size)]
        self.__Start = -1
        self.__NextFree = 0
        for i in range(30 - 1):
            self.__Node[i].setPointer(i + 1)                # points to next node

    def AddNode(self):
        newItem = input("Enter new item here: ")
        self.__Node[self.__NextFree].setData(newItem)

        if self.__Start == -1:
            self.__Start = self.__NextFree
            temp = self.__Node[self.__NextFree].getPointer()
            self.__Node[self.__NextFree].setPointer(-1)
            self.__NextFree = temp
        else:
            temp = self.__Node[self.__NextFree].getPointer()
            if newItem < self.__Node[self.__Start].getData():
                self.__Node[self.__NextFree].setPointer(self.__Start)
                self.__Start = self.__NextFree
                self.__NextFree = temp
            else:
                previous = self.__Start
                current = self.__Start
                found = False

                while (found == False and current != -1):
                    if newItem <= self.__Node[current].getData():
                        self.__Node[previous].setPointer(self.__NextFree)
                        self.__Node[self.__NextFree].setPointer(current)
                        self.__NextFree = temp
                        found = True
                    else:
                        previous = current
                        current = self.__Node[current].getPointer()

                if current == -1:
                    self.__Node[previous].setPointer(self.__NextFree)
                    self.__Node[self.__NextFree].setPointer(-1)
                    self.__NextFree = temp

    def RemoveNode(self):
        ToRemove = input("Enter the item to remove: ")
        if self.IsEmpty():
            print("Cannot remove from the linked list as linked list is empty.")
        else:
            if self.__Node[self.__Start].getData() == ToRemove:         #  one to be removed is the first node
                temp = self.__NextFree
                self.__NextFree = self.__Start
                self.__Start = self.__Node[self.__Start].getPointer()
                self.__Node[self.__NextFree].setPointer(temp)
            else:
                previous = self.__Start
                current = self.__Start
                found = False

                while (found == False and current != -1):
                    if self.__Node[current].getData() == ToRemove:
                        temp = self.__NextFree
                        self.__Node[previous].setPointer(self.__Node[current].getPointer())
                        self.__NextFree = current
                        self.__Node[self.__NextFree].setPointer(temp)
                        found = True
                    else:
                        previous = current
                        current = self.__Node[current].getPointer()

                if current == -1:
                    print("Item not found in linked list, cannot delete.") 

    def Traversal(self):
        index = self.__Start
        self.__TraversalInOrder(index)

    def __TraversalInOrder(self, index):
        if index != -1:
            print(self.__Node[index].getData())
            self.__TraversalInOrder(self.__Node[index].getPointer())
            
    def ReverseTraversal(self):
        index = self.__Start
        self.__TraversalInReverseOrder(index)

    def __TraversalInReverseOrder(self, index):
        if index != -1:
            self.__TraversalInReverseOrder(self.__Node[index].getPointer())
            print(self.__Node[index].getData())

    def DisplayLinkedList(self):
        print("|  Node  |                    Data                    |  Pointer  |\n" + \
              "-------------------------------------------------------------------")
        for i in range(len(self.__Node)):
            print("|{0:^8}|{1:^44}|{2:^11}|".format(i, self.__Node[i].getData(), self.__Node[i].getPointer()))
        print()
        print("Start:    {0}".format(self.__Start))
        print("NextFree: {0}".format(self.__NextFree))
        print()
        print()

    def IsEmpty(self):
        return (self.__NextFree == -1)

    def IsFull(self):
        return (self.__Start == -1)

def main():
    fruits = LinkedList()
    while True:
        print("1.   Add an item\n" + \
              "2.   Traverse the linked list of used nodes and output the data values\n" + \
              "3.   Output all pointers and data values\n" + \
              "4.   Traverse the linked list of used nodes and output the data values, in reverse order\n" + \
              "5.   Remove an item from the linked list\n" + \
              "X.   Exit")
        option = input("Enter option: ")
        if option == '1':
            fruits.AddNode()
        elif option == '2':
            fruits.Traversal()
        elif option == '3':
            fruits.DisplayLinkedList()
        elif option == '4':
            fruits.ReverseTraversal()
        elif option == '5':
            fruits.RemoveNode()
        elif option == 'X':
            break
        else:
            print("Invalid input.\n")
