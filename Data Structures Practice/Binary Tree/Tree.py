class Node:
    def __init__(self, data, leftChild = None, rightChild = None):
        self.__data = data
        self.__leftChild = None
        self.__rightChild = None

    def getData(self):
        return self.__data
    def getLeftChild(self):
        return self.__leftChild
    def getRightChild(self):
        return self.__rightChild
    def setRootData(self, data):
        self.__rootData = data
    def setLeftChild(self, child):
        self.__leftChild = child
    def setRightChild(self, child):
        self.__rightChild = child

class BinaryTree:
    def __init__(self):
        self.__start = None

    def getStart(self):
        return self.__start

    def insert(self, data):
        newNode = Node(data)
        if self.__start == None:     # empty BST
            self.__start = newNode
        else:
            current = self.__start
            previous = self.__start
            while current:
                if data < current.getData():        # move left branch
                    previous = current
                    current  = current.getLeftChild()
                else:
                    previous = current
                    current  = current.getRightChild()
            if data < previous.getData():
                previous.setLeftChild(newNode)
            else:
                previous.setRightChild(newNode)

    def preOrder(self, current):
        if current:
            print(current.getData(), end=', ')
            self.preOrder(current.getLeftChild())
            self.preOrder(current.getRightChild())

    def inOrder(self, current):
        if current:
            self.inOrder(current.getLeftChild())
            print(current.getData(), end=', ')
            self.inOrder(current.getRightChild())

    def postOrder(self, current):
        if current:
            self.postOrder(current.getLeftChild())
            self.postOrder(current.getRightChild())
            print(current.getData(), end=', ')

    def search(self, key):
        current = self.__start
        while current:    # empty BST
            if key == current.getData():
                return "{} is found in the tree!".format(key)
            elif key < current.getData():
                current = current.getLeftChild()
            else:
                current = current.getRightChild()
        return "{} is not found in the tree.".format(key)

    def delete(self, key):      # go infinite loop yourself, therefore it is obviously not working
        previous = None
        current = self.__start
        while current:    # empty BST
            if key == current.getData():
                break
            elif key < current.getData():
                previous = current
                current  = current.getLeftChild()
            else:
                previous = current
                current  = current.getRightChild()
        if current == None:
            print("{} is not found in the tree, cannot delete.".format(data))
            return
        else:
            if current.getLeftChild() == None and current.getRightChild() == None:
                if previous.getData() < current.getData():
                    previous.setLeftChild(None)
                else:
                    previous.setRightChild(None)
            elif current.getLeftChild() == None:
                temp = current.getRightChild()
                if previous.getData() < current.getData():
                    previous.setLeftChild(temp)
                else:
                    previous.setRightChild(temp)
                
            elif current.getRightChild() == None:
                temp = current.getLeftChild()
                if previous.getData() < current.getData():
                    previous.setLeftChild(temp)
                else:
                    previous.setRightChild(temp)

            else:
                temp = current.getRightChild()
                while temp:
                    temp = current.getLeftChild()
                temp.setRightChild(current.getRightChild())
                previous.setRightChild(temp)
            return


        
    
def main():
    countries = ["Japan", "Singapore", "India", "China", "Sweden", "USA", "Australia", "UK", "Germany"]
    counTree = BinaryTree()
    for country in countries:
        counTree.insert(country)
    print(" Pre-order: ", end='')
    counTree.preOrder(counTree.getStart())
    print()
    print("  In-order: ", end='')
    counTree.inOrder(counTree.getStart())
    print()
    print("Post-order: ", end='')
    counTree.postOrder(counTree.getStart())
    print()
    counTree.delete("UK")
    print(counTree.search("Korea"))
    print(counTree.search("Malaysia"))
    for country in countries:
        print(counTree.search(country))
