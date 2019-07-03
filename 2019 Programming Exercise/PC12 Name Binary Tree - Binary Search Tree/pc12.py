class Node:
    def __init__(self, data):   # constructor()
        self.__data = str(data)
        self.__leftPtr = int(-1)
        self.__rightPtr = int(-1)

    def setData(self, s):
        self.__data = str(s)

    def setLeftPtr(self, x):
        self.__leftPtr = int(x)

    def setRightPtr(self, y):
        self.__rightPtr = int(y)

    def getData(self):
        return self.__data

    def getLeftPtr(self):
        return self.__leftPtr

    def getRightPtr(self):
        return self.__rightPtr
    
class Tree:
    '''NOTE: This is a binary search tree that assumes that there is no limit to the number of nodes that can be added to the tree.'''
    def __init__(self):         # constructor() / CreateNewTree method
        self.__tree = []
        self.__root = -1

    def add(self, newItem):
        newNode = Node(newItem)
        if self.__root == -1:
            self.__root = 0
            self.__tree.append(newNode)
        else:
            previous = self.__root
            current = self.__root
            while current != -1:
                if newItem < self.__tree[current].getData():
                    previous = current
                    current = self.__tree[current].getLeftPtr()
                else:
                    previous = current
                    current = self.__tree[current].getRightPtr()
            self.__tree.append(newNode)                 # new index of node is (length of new tree - 1)
            if newItem < self.__tree[previous].getData():
                self.__tree[previous].setLeftPtr(len(self.__tree) - 1)
            else:
                self.__tree[previous].setRightPtr(len(self.__tree) - 1)

    def __str__(self):          # print() method
        output = "Root of tree: {0}\n".format(self.__root)
        output += "-" * 63
        output += "\n"
        output += "| {0:^10} | {1:^20} | {2:^10} | {3:^10} |\n".format("Index", "Data", "Left Ptr", "Right Ptr")
        output += "-" * 63
        output += "\n"
        for i in range(len(self.__tree)):
            current = self.__tree[i]     # current nodde
            output += "| {0:^10} | {1:^20} | {2:^10} | {3:^10} |\n".format(i, current.getData(), current.getLeftPtr(), current.getRightPtr())
        output += "-" * 63
        output += "\n\n"
        return output

    def inOrderTraversal(self, index):
        if index != -1:
            self.inOrderTraversal(self.__tree[index].getLeftPtr())
            print(self.__tree[index].getData())
            self.inOrderTraversal(self.__tree[index].getRightPtr())

    def getRoot(self):
        return self.__root
            

def main():
    peopleTree = Tree()
    peopleList = ["Dave", "Fred", "Ed", "Greg", "Bob", "Cid", "Ali"]
    for person in peopleList:
        peopleTree.add(person)
    print(peopleTree)
    peopleTree.inOrderTraversal(peopleTree.getRoot())
        
