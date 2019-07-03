class Node:
    def __init__(self, Data):
        self.__LeftP  = int(0)
        self.__Data   = str(Data)
        self.__RightP = int(0)

    def GetLeftP(self):
        return self.__LeftP

    def GetRightP(self):
        return self.__RightP

    def GetData(self):
        return self.__Data

    def SetLeftP(self, LeftP):
        self.__LeftP  = int(LeftP)

    def SetRightP(self, RightP):
        self.__RightP = int(RightP)

    def SetData(self, Data):
        self.__Data   = str(Data)

class BinaryTree:
    def __init__(self):
        self.__ThisTree = [Node("") for i in range(20 + 1)]
        self.__Root = 0
        self.__NextFreePosition = 1
        for i in range(1, 20):
            self.__ThisTree[i].SetLeftP(i + 1)

    def AddItemToBinaryTree(self, NewTreeItem):
        if self.__NextFreePosition == 0:        # binary tree is full
            print("No space available, cannot add to binary tree!")
            return
        else:
            temp = self.__ThisTree[self.__NextFreePosition].GetLeftP()
            self.__ThisTree[self.__NextFreePosition].SetData(NewTreeItem)    # assign NewTreeItem to next free position to be inserted
            self.__ThisTree[self.__NextFreePosition].SetLeftP(0)
            self.__ThisTree[self.__NextFreePosition].SetRightP(0)# no effect because RightP already 0
            LastMove = 'X'           
            if self.__Root == 0:
                self.__Root = self.__NextFreePosition
            else:
                CurrentPosition = self.__Root
                LastMove = 'X'
                while CurrentPosition != 0:
                    PreviousPosition = CurrentPosition
                    if NewTreeItem < self.__ThisTree[CurrentPosition].GetData():
                        # move left
                        LastMove = 'L'
                        CurrentPosition = self.__ThisTree[CurrentPosition].GetLeftP()
                    else:
                        # move right
                        LastMove = 'R'
                        CurrentPosition = self.__ThisTree[CurrentPosition].GetRightP()
            if LastMove == 'R':
                self.__ThisTree[PreviousPosition].SetRightP(self.__NextFreePosition)
            elif LastMove == 'L':
                self.__ThisTree[PreviousPosition].SetLeftP(self.__NextFreePosition)
            self.__NextFreePosition = temp

    def OutputData(self):
        print("Value of Root:             {0}".format(self.__Root))
        print("Value of NextFreePosition: {0}".format(self.__NextFreePosition))
        print()
        print("-" * 73)
        print("| {0:^10} | {1:^15} | {2:^20} | {3:^15} |".format("Index", "Left Pointer", "Data", "Right Pointer"))
        print("-" * 73)
        for i in range(1, 21):
            CurrentNode = self.__ThisTree[i]
            print("| {0:^10} | {1:^15} | {2:^20} | {3:^15} |".format(i, CurrentNode.GetLeftP(), CurrentNode.GetData(), CurrentNode.GetRightP()))
        print("-" * 73)

    def TraverseInOrderFromRoot(self):                  # function to traverse in-order from root
        self.TraverseInOrder(self.__Root)

    def TraverseInOrder(self, index):
        if index != 0:
            self.TraverseInOrder(self.__ThisTree[index].GetLeftP())
            print(self.__ThisTree[index].GetData())
            self.TraverseInOrder(self.__ThisTree[index].GetRightP())
            

def main():
    CountryBinaryTree = BinaryTree()
    while True:
        CurrentInput = input("Enter a new data item to insert to the binary tree (XXX to stop): ")
        if CurrentInput == "XXX":
            break
        else:
            CountryBinaryTree.AddItemToBinaryTree(CurrentInput)
    CountryBinaryTree.OutputData()
    CountryBinaryTree.TraverseInOrderFromRoot()
              
            
