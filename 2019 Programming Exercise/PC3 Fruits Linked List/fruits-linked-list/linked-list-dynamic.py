class ListNode:
    def __init__(self, data = "", pointer= -1):
        self.__DataValue = data
        self.__PointerValue = pointer

    def getData(self):
        return self.__DataValue

    def getPointer(self):
        return self.__PointerValue

    def setData(self, NewData):
        self.__DataValue = NewData

    def setPointer(self, NewPointer):
        self.__PointerValue = NewPointer

class LinkedList:
    def __init__(self):
        self.__Start = None                          # dynamic linked list
        self.__Node = []

    def InsertFront(self, data):                    # O(1)
        NewNode = ListNode(data, self.__Start)
        self.__Start = NewNode

    def InsertAtIndex(self, data, index):
        current = self.__Start
        if index == 0:
            self.InsertFront(data)
        else:
            for i in range(index - 1):
                current = current.getPointer()
                if current == None:
                    print("Cannot insert at index {0}, as list has less than {0} elements.".format(index))
                    return
            NewNode = ListNode(data, current.getPointer())
            current.setPointer(NewNode)

    def InsertBack(self, data):                     # O(n)
        current = self.__Start
        while current.getPointer() != None:
            current = current.getPointer()
        NewNode = ListNode(data, None)
        current.setPointer(NewNode)

    def ListAllNodes(self):
        current = self.__Start
        while current != None:
            print(current.getData())
            current = current.getPointer()

def main():
    a = LinkedList()
    a.InsertFront("1st inserted from front")
    a.InsertBack("1st inserted from back")
    a.InsertBack("2nd inserted from back")
    a.InsertFront("2nd inserted from front")
    a.InsertAtIndex("Inserted at index 0", 0)
    a.InsertAtIndex("Inserted at index 3", 3)
    a.InsertAtIndex("Inserted at index 54?", 6)
    a.ListAllNodes()
