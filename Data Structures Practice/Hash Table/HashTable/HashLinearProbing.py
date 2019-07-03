''' A hash table that makes use of linear probing to handle collisions '''
class HashTable:
    def __init__(self, size = 10):
        self.__table = [None for i in range(size)]
        
    def __hash(self, data):
        hash_value = 0
        for character in data:
            hash_value += ord(character)
        hash_value %= len(self.__table)
        return hash_value

    def __str__(self):
        result = "\n| {0:^10} | {1:^40} |\n".format("Hash", "Value")
        result += "-" * 57
        result += "\n"
        for i in range(len(self.__table)):
            if self.__table[i] == None:
                result += "| {0:^10} | {1:^40} |\n".format(i, ">>>> No data added yet. <<<<")
            else:
                result += "| {0:^10} | {1:^40} |\n".format(i, self.__table[i])
        return result

    def insert(self, NewData):
        index = self.__hash(NewData)
        while self.__table[index] != None:
            if index == len(self.__table) - 1:                  # last element
                index = 0
            else:
                index += 1
            if index == self.__hash(NewData):                  # one loop done
                print("hash table is full, therefore linear probing is useless")
                return
        self.__table[index] = NewData

    def FindIndex(self, SearchKey):
        index = self.__hash(SearchKey)
        while self.__table[index] != SearchKey:
            if index == len(self.__table) - 1:                  # last element
                index = 0
            else:
                index += 1
            if index == self.__hash(SearchKey):                # one loop done
                index = None
                break
        return index

    def IsFound(self, SearchKey):
        return self.FindIndex(SearchKey) != None

    def search(self, SearchKey):
        if not self.IsFound(SearchKey):
            print("The search key, '{0}', is not found in the hash table.".format(SearchKey))
        else:
            print("The search key, '{0}', is found in the hash table.".format(SearchKey))

    def remove(self, data):
        if not self.IsFound(data):
            print("The data to remove, '{0}', is not found in the hash table, hence it cannot be removed.".format(data))
        else:
            index = self.FindIndex(data)
            self.__table[index] = None

def main():
    a = HashTable(3)
    a.insert("yeet")
    a.insert("grey")
    a.insert("yeah boy")
    a.insert("oof")
    a.insert("hello wqorld")
    a.insert("oh no")
    a.search("asasa")
    a.search("yeet")
    a.search("oh no")
    print(a)
    a.remove("oh no")
    a.remove("oh noes")
    a.remove("")
    print(a)

def main2():
    b = HashTable(11)
    b.insert("apple")
    b.insert("pear")
    b.insert("banana")
    b.insert("kiwi")
    b.insert("orange")
    b.insert("papaya")
    print(b)
    b.remove("orange")
    b.remove("banana")
    b.remove("yeet")
    print(b)
    b.search("orange")
    b.search("yeet")
    b.search("pear")

# everything is ~O(1) except when deleting or removing when data is not found which is O(n)
