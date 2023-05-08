class Node:
    def __init__(self, DataValue = "", LeftChild = -1, RightChild = -1):
        self.__DataValue = str(DataValue)
        self.__LeftChild = int(LeftChild)
        self.__RightChild = int(RightChild)

    def SetDataValue(self, DataValue = ""):
        self.__DataValue = str(DataValue)

    def GetDataValue(self):
        return self.__DataValue

    def SetLeftChild(self, LeftChild = -1):
        self.__LeftChild = int(LeftChild)

    def GetLeftChild(self):
        return self.__LeftChild

    def SetRightChild(self, RightChild = -1):
        self.__RightChild = int(RightChild)

    def GetRightChild(self):
        return self.__RightChild

class ExpressionTree:
    def __init__(self):
        self.__Tree = [Node() for i in range(20)]
        self.__Fringe = []
        self.__Root = 0
        self.__NextFreeChild = 0
        for i in range(20 - 1):
            self.__Tree[i].SetLeftChild(i + 1)

    def Insert(self, NewToken):
        if self.__NextFreeChild == -1: #check if tree is full
            return "Tree is full"

        # tree is not full, safe to insert new token
        if self.__NextFreeChild == 0:
            self.__Tree[self.__Root].SetDataValue(NewToken)
            self.__NextFreeChild = self.__Tree[self.__Root].GetLeftChild()
            self.__Tree[self.__Root].SetLeftChild(-1)
        else:
            #inserting into tree with existing nodes
            #starting with Root
            Current = 0     # index of the current node
            Previous = -1   # index of the previous node
            NewNode = self.__Tree[self.__NextFreeChild] # declare new node
            NewNode.SetDataValue(NewToken)

            # finding the node at which the NewNode can be inserted
            while Current != -1:
                CurrNode = self.__Tree[Current]
                if IsOperator(CurrNode.GetDataValue()):
                # check if CurrNode contains an operator
                    if CurrNode.GetLeftChild() == -1:
                        # if LeftChild is empty, insert here
                        CurrNode.SetLeftChild(self.__NextFreeChild)
                        self.__NextFreeChild = NewNode.GetLeftChild()
                        NewNode.SetLeftChild(-1)
                        Current = -1
                    elif CurrNode.GetRightChild() == -1:
                        # if RightChild is empty, insert here
                        CurrNode.SetRightChild(self.__NextFreeChild)
                        self.__NextFreeChild = NewNode.GetLeftChild()
                        NewNode.SetLeftChild(-1)
                        Current = -1
                    elif IsOperator(self.__Tree[CurrNode.GetLeftChild()].GetDataValue()):
                        # if LeftChild is an operator,
                        # traverse leftchild subtree
                        Previous = Current
                        Current = CurrNode.GetLeftChild()
                        self.__Fringe.append(Previous)
                    elif IsOperator(self.__Tree[CurrNode.GetRightChild()].GetDataValue()):
                        # if RightChild is an operator,
                        # traverse rightchild subtree
                        Previous = Current
                        Current = CurrNode.GetRightChild()
                        self.__Fringe.append(Previous)
                    else:
                        #traverse right subtree
                        Previous = self.__Fringe.pop(-1)
                        Current = self.__Tree[Previous].GetRightChild()
                else:
                    #no place to insert
                    return "Cannot be inserted"

    def Display(self):
        print("         Root:", self.__Root)
        print("NextFreeChild:", self.__NextFreeChild)
        print()
        # print heading
        print("-" * 93)
        print("| {0:^10} | {1:^20} | {2:^30} | {3:^20} |".format("Index", "Left Child", "Data Value", "Right Child"))
        print("-" * 93)
        for i in range(len(self.__Tree)):
            LeftChild = self.__Tree[i].GetLeftChild()
            RightChild = self.__Tree[i].GetRightChild()
            Data = self.__Tree[i].GetDataValue()
            print("| {0:^10} | {1:^20} | {2:^30} | {3:^20} |".format(i, LeftChild, Data, RightChild))
        print("-" * 93)
        print()

    def infix(self):
        self.InOrderTraverse(self.__Root)
        print()
        
    def InOrderTraverse(self, index):
        index = int(index)
        if index != -1:
            self.InOrderTraverse(self.__Tree[index].GetLeftChild())
            print(self.__Tree[index].GetDataValue(), end = ' ')
            self.InOrderTraverse(self.__Tree[index].GetRightChild())

    def calculate(self):
        print("Numerical answer to expression: {0:.2f}".format(self.CalculateFromIndex(self.__Root)))

    def CalculateFromIndex(self, index = 0):
        CurrentValue = self.__Tree[index].GetDataValue()
        
        # if current node is an operator,
        # do certain operations on the 2 branches
        if IsOperator(CurrentValue):
            if CurrentValue == "+":
                return self.CalculateFromIndex(self.__Tree[index].GetLeftChild()) + \
                       self.CalculateFromIndex(self.__Tree[index].GetRightChild())
            elif CurrentValue == "-":
                return self.CalculateFromIndex(self.__Tree[index].GetLeftChild()) - \
                       self.CalculateFromIndex(self.__Tree[index].GetRightChild())
            elif CurrentValue == "*":
                return self.CalculateFromIndex(self.__Tree[index].GetLeftChild()) * \
                       self.CalculateFromIndex(self.__Tree[index].GetRightChild())
            elif CurrentValue == "/":
                return self.CalculateFromIndex(self.__Tree[index].GetLeftChild()) / \
                       self.CalculateFromIndex(self.__Tree[index].GetRightChild())
        else:
            return int(CurrentValue)
            
def IsOperator(s):
    if (len(s) == 1 and s in "+-*/"):
        return True
    else:
        return False


Tree = ExpressionTree()
Tree.Insert("+")
Tree.Insert("*")
Tree.Insert("4")
Tree.Insert("2")
Tree.Insert("/")
Tree.Insert("3")
Tree.Insert("1")
Tree.Display()
Tree.infix()
Tree.calculate()
        
