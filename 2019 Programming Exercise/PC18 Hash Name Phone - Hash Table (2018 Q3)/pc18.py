## TASK 1
class Record:
    def __init__(self, PersonName = "", TelephoneNumber = ""):
        self.__PersonName = str(PersonName)
        self.__TelephoneNumber = str(TelephoneNumber)

    def SetPersonName(self, NewPersonName = ""):
        self.__PersonName = str(NewPersonName)

    def SetTelephoneNumber(self, NewTelephoneNumber = ""):
        self.__TelephoneNumber = str(NewTelephoneNumber)

    def GetPersonName(self):
        return self.__PersonName

    def GetTelephoneNumber(self):
        return self.__TelephoneNumber

# assume that this hash table has a fixed size of 500 records.
class HashTable:
    def __init__(self):
        # creates a Python list of records.
        self.__Data = [Record() for i in range(500)]

    def AddRecord(self, index = 0, NewRecord = Record()):
        self.__Data[index] = NewRecord

    ## TASK 2
    # in class HashTable
    def DisplayValues(self):
        #print heading
        print("-" * 70)
        print("| {0:^10} | {1:^30} | {2:^20} |".format("Index", "PersonName", "TelephoneNumber"))
        print("-" * 70)
        
        for index in range(len(self.__Data)):
            current = self.__Data[index]        # the current record with index 'index'
            name    = current.GetPersonName()
            telno   = current.GetTelephoneNumber()

            # print record only when name or telephone number or both are filled up
            if name != "" or telno != "":          
                print("| {0:^10} | {1:^30} | {2:^20} |".format(index, name, telno))
            
        print("-" * 70)

    def Search(self, SearchName):
        index  = GenerateHash(SearchName)
        found  = False
        while self.__Data[index].GetPersonName() != "":   # record is not empty
            if self.__Data[index].GetPersonName() == SearchName:
                found = True
                telno = self.__Data[index].GetTelephoneNumber()
                break
            else:
                index += 1
        if found:
            print("The name, " + SearchName + ", is found:")
            print()
            #print heading
            print("-" * 70)
            print("| {0:^10} | {1:^30} | {2:^20} |".format("Index", "PersonName", "TelephoneNumber"))
            print("-" * 70)
            print("| {0:^10} | {1:^30} | {2:^20} |".format(index, SearchName, telno))
            print("-" * 70)
        else:
            print("The name, " + SearchName + ", is NOT FOUND.")
            

## TASK 3
# outside of class HashTable
def GenerateHash(SearchName):
    SearchName = str(SearchName)
    HashTotal  = 0
    for i in range(len(SearchName)):
        character  = SearchName[i]
        code       = ord(character)
        code      *= (i + 1)
        HashTotal += code

    Hash = HashTotal % 500
    return Hash

## TASK 2
Table = HashTable()
HashFile = open("HASHEDDATA.txt", "r")
for line in HashFile:
    if line[-1] == "\n":
        line = line[:-1]        # remove newline
    index, name, telno = line.split(",")
    index = int(index)
    name  = str(name)
    telno = str(telno)
    
    record = Record(name, telno)
    Table.AddRecord(index, record)

HashFile.close()
Table.DisplayValues()

SearchName = input("Enter the name to search for: ")
Table.Search(SearchName)

