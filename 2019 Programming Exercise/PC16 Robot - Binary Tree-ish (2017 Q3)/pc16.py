########    TASK 1    ########

class ConnectionNode:
    def __init__(self, DataValue = "", LeftChild = 0, RightChild = 0):
        self.__DataValue  = str(DataValue)
        self.__LeftChild  = int(LeftChild)
        self.__RightChild = int(RightChild)

    def SetDataValue(self, NewDataValue = ""):
        self.__DataValue = str(NewDataValue)

    def SetLeftChild(self, NewLeftChild = 0):
        self.__LeftChild = int(NewLeftChild)

    def SetRightChild(self, NewRightChild = 0):
        self.__RightChild = int(NewRightChild)

    def GetDataValue(self):
        return self.__DataValue

    def GetLeftChild(self):
        return self.__LeftChild

    def GetRightChild(self):
        return self.__RightChild

class LinkedList:
    def __init__(self):
        
        # index 0 is None since this data structure will be 1-based
        self.__RobotData = [None] + [ConnectionNode() for i in range(25)]
        self.__Root = 1
        self.__NextFreeChild = 1
        for i in range(1, 25):
            self.__RobotData[i].SetLeftChild(i + 1)

    ########    TASK 2    ########
    def FindNode(self, NodeValue):
        Found = False
        CurrentPosition = self.__Root
        while Found != True and CurrentPosition <= 25:
            if self.__RobotData[CurrentPosition].GetDataValue() == NodeValue:
                Found = True
            else:
                CurrentPosition += 1
        if CurrentPosition > 25:
            return 0
        else:
            return CurrentPosition

    def AddToRobotData(self, NewDataItem, ParentItem, ThisMove):
        if self.__Root == 1 and self.__NextFreeChild == 1:
            self.__NextFreeChild = self.__RobotData[self.__NextFreeChild].GetLeftChild()
            self.__RobotData[self.__Root].SetLeftChild(0)
            self.__RobotData[self.__Root].SetDataValue(NewDataItem)
        else:
            # does the parent exist?
            ParentPosition = self.FindNode(ParentItem)
            if ParentPosition > 0:
                # does the child exist?
                ExistingChild = self.FindNode(NewDataItem)
                if ExistingChild > 0:       # child exists
                    ChildPointer = ExistingChild
                else:
                    ChildPointer = self.__NextFreeChild
                    self.__NextFreeChild = self.__RobotData[self.__NextFreeChild].GetLeftChild()
                    self.__RobotData[ChildPointer].SetLeftChild(0)
                    self.__RobotData[ChildPointer].SetDataValue(NewDataItem)
                if ThisMove == 'L':
                    self.__RobotData[ParentPosition].SetLeftChild(ChildPointer)
                else:
                    self.__RobotData[ParentPosition].SetRightChild(ChildPointer)

    ########    TASK 3    ########
    def OutputData(self):
        print("         Value of Root: ", self.__Root)
        print("Value of NextFreeChild: ", self.__NextFreeChild)
        print()

        # print heading
        print("-" * 63)
        print("{0:^10}|{1:^15}|{2:^20}|{3:^15}".format("Index", "Left Pointer", "Data Value", "Right Pointer"))
        print("-" * 63)
        for i in range(1, 26):
            CurrentNode = self.__RobotData[i]
            print("{0:^10}|{1:^15}|{2:^20}|{3:^15}".format(i, CurrentNode.GetLeftChild(), CurrentNode.GetDataValue(),\
                                                           CurrentNode.GetRightChild()))
        print("-" * 63)

    ########    TASK 5    ########
    def GetRoot(self):
        return self.__Root

    # RoutePath is an array containing all valid routes from A to Z.
    def PreOrderTraversal(self, Index, RoutePath):
        if Index != 0:
            RoutePath += [self.__RobotData[Index].GetDataValue()]
            self.PreOrderTraversal(self.__RobotData[Index].GetLeftChild(), RoutePath)
            self.PreOrderTraversal(self.__RobotData[Index].GetRightChild(), RoutePath)
            
########    TASK 4    ########
def main():
    Robot = LinkedList()
    SearchFile = open("SEARCHTREE.TXT", "r")
    for line in SearchFile:
        if line[-1] == "\n":
            line = line[:-1]
            
        RouteData   = line.split(",")
        NewDataItem = RouteData[0]
        ParentItem  = RouteData[1]
        ThisMove    = RouteData[2]
        Robot.AddToRobotData(NewDataItem, ParentItem, ThisMove)

    Robot.OutputData()

    ########    TASK 5    ########
    RoutePath = []
    Robot.PreOrderTraversal(Robot.GetRoot(), RoutePath)
    print(" ".join(RoutePath))

