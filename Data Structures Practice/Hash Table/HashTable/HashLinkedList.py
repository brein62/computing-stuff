class LinkedListNode:
    def __init__(self, Data, Pointer):
        self.__Data = Data
        self.__Pointer = Pointer

    def GetData(self):
        return self.__Data
    
    def GetPointer(self):
        return self.__Pointer
    
    def SetData(self, NewData):
        self.__Data = NewData
        
    def SetPointer(self, NewPointer):
        self.__Pointer = NewPointer

class LinkedList:
    def __init__(self):
        self.__Start = None

    def __str__(self):
        result = ""
        curr = self.__Start
        if self.__Start == None:
            result = "None"
            return result
        else:
            while curr != None:
                result += curr.GetData()
                if curr != None:
                    result += " -> "
                curr = curr.GetPointer()
            result += "None"
            return result

    def insert(self, Data):
        NewNode = LinkedListNode(Data, None)
        if self.__Start == None:            # empty
            self.__Start = NewNode
        else:
            prev = self.__Start
            while prev.GetPointer() != None:
                prev = prev.GetPointer()
            prev.SetPointer(NewNode)

    def remove(self, data):
        if self.__Start == None:
            print("The linked list is empty.")
        else:
            prev = self.__Start
            curr = self.__Start
            while curr != None and curr.GetData() != data:
                prev = curr
                curr = curr.GetPointer()
            if curr != None:
                if curr.GetData() == data:
                    # can remove
                    prev.SetPointer(curr.GetPointer())
            else:
                print("The data cannot be found.")

    def search(self, data):
        curr = self.__Start
        while curr != None:
            if curr.GetData() == data:
                return True
            curr = curr.GetPointer()
        return False

class HashTable:
    def __init__(self, size = 10):
        self.__table = [LinkedList() for i in range(size)]

    def __hash(self, data):
        hash_value = 0
        for character in data:
            hash_value += ord(character)
        hash_value %= len(self.__table)
        return hash_value

    def __str__(self):
        result = ""
        for i in range(len(self.__table)):
            result += str(i)
            result += ": "
            result += str(self.__table[i])
            result += "\n"
        return result
            
    def insert(self, NewData):
        index = self.__hash(NewData)
        self.__table[index].insert(NewData)

    def remove(self, data):
        index = self.__hash(data)
        self.__table[index].remove(data)

    def search(self, key):
        index = self.__hash(key)
        if self.__table[index].search(key) == True:     # found in the linked list
            print("{0} is found in the hash table at index {1}.".format(key, index))
        else:
            print("{0} is not found in the hash table.".format(key))
        

def main():
    a = HashTable(5)
    a.insert("yeet")
    a.insert("grey")
    a.insert("yeah boy")
    a.insert("oof")
    a.search("oof")
    a.insert("hello world")
    print(a)
    a.remove("oof")
    a.search("oof")
    print(a)
