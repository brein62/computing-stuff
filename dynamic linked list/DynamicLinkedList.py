class ListNode:
    def __init__(self, data = "", pointer = None):
        self.__Data = data
        self.__Pointer = pointer

    def SetData(self, NewData):
        self.__Data = NewData

    def SetPointer(self, NewPointer):
        self.__Pointer = NewPointer

    def GetData(self):
        return self.__Data

    def GetPointer(self):
        return self.__Pointer

class DynamicLinkedList:
    def __init__(self):
        self.__Start = None

        # # # # # # # # # # # # # # # # # # # # # #
        # None represents the ending pointer.     #
        # Since there are no nodes in the empty   #
        # linked list, the starting pointer       #
        # would be None as a result.              #
        # # # # # # # # # # # # # # # # # # # # # #

    def AddToFront(self, NewData):
        NewNode = ListNode(NewData, self.__Start)                   # add this to the front of the current start node
        self.__Start = NewNode                                      # set this node as the starting node

    def AddToBack(self, NewData):
        NewNode = ListNode(NewData, None)                           # as this is at the back, the node points to the ending pointer, None.

        ## TRAVERSE THE LINKED LIST ##
        Previous = self.__Start
        Current = self.__Start

        while (Current != None):                                    # stops when Current == None and Previous is the last node in the linked list
            Previous = Current                                      # makes Previous the next pointer
            Current = Current.GetPointer()                          # makes Current the next pointer

        Previous.SetPointer(NewNode)                                # set the previous pointer as the new node

    ## NOTE: ONLY WORKS WELL IF YOU DON'T USE THE TWO INSERTING FUNCTIONS ABOVE ##
    def AddInPlace(self, NewData):
        NewNode = ListNode(NewData)
        if (self.__Start == None):                                  # linked list is empty
            NewNode.SetPointer(None)                                # sets the new node pointer as None
            self.__Start = NewNode                                  # sets the starting node pointer as NewNode
        else:
            if (NewData < self.__Start.GetData()):                  # belongs at the front
                NewNode.SetPointer(self.__Start)                    # sets the pointer as the current starting node before addition
                self.__Start = NewNode                              # sets the starting node as NewNode
            else:                                                   # belongs elsewhere in the linked list
                ## TRAVERSE THE LINKED LIST ##
                Previous = self.__Start
                Current = self.__Start
                while (Current != None and Current.GetData() < NewData):
                    Previous = Current                                      # makes Previous the next pointer
                    Current = Current.GetPointer()                          # makes Current the next pointer

                NewNode.SetPointer(Current)                                 # sets the new pointer as Current
                Previous.SetPointer(NewNode)                                # set the previous pointer as the new node

    def DisplayInOrder(self):
        Current = self.__Start
        while (Current != None):
            print(Current.GetData())
            Current = Current.GetPointer()

    def Remove(self, DataToRemove):
        ## TRAVERSE THE LINKED LIST ##
        Previous = self.__Start
        Current = self.__Start
        while (Current != None and Current.GetData() != DataToRemove):
            Previous = Current                                      # makes Previous the next pointer
            Current = Current.GetPointer()                          # makes Current the next pointer

        if (Current == None):
            print("The node to remove, {}, doesn't exist.".format(DataToRemove))
        else:
            NextPointer = Current.GetPointer()                      # pointer after the element to remove
            Previous.SetPointer(NextPointer)
        
                
def main():         # driver program
    LinkedList1 = DynamicLinkedList()
    NewData1 = input("Enter data here: ")
    LinkedList1.AddInPlace(NewData1)
    NewData2 = input("Enter data here: ")
    LinkedList1.AddInPlace(NewData2)
    NewData3 = input("Enter data here: ")
    LinkedList1.AddInPlace(NewData3)
    NewData4 = input("Enter data here: ")
    LinkedList1.AddInPlace(NewData4)
    NewData5 = input("Enter data here: ")
    LinkedList1.AddInPlace(NewData5)
    NewData6 = input("Enter a node to remove: ")
    LinkedList1.Remove(NewData6)
    LinkedList1.DisplayInOrder()
    
main()
