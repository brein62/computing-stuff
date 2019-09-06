# A Level Computing 2015 Paper's Confusing Af Stuff

import random

def RandomLetter():
    # also can use random.randint(0, 25)
    LetterIndex = int(random.random() * 26)

    # 'A': 65, 'B': 66, ...
    return chr(LetterIndex + 65)

def LicenceKey():
    Key = ""
    ASCIISum = 0

    # i = 1, 2, 3, ..., 9, 10 : weights for the ASCII sum
    for i in range(1, 10):
        Letter = RandomLetter()
        Key      += Letter
        ASCIISum += (ord(Letter) * i)

    # remainder from dividing total by 11
    ASCIIRem = ASCIISum % 11
    if ASCIIRem == 10:
        Key += "X"
    else:
        Key += str(ASCIIRem)

    return Key
    
def main():
    while True:

        # print menu
        print("1. Purchase of a new licence for either a single-user or 3-user licence")
        print("2. Register an additional user to an active 3-user licence")
        print("3. End")
        print()

        while True:
            option = input(">>> ")
            if option == "1":
                BuyNewLicence()
                break
            elif option == "2":
                RegisterUser()
                break
            elif option == "3":
                return              # exit out of menu
            else:
                print("Invalid option selected!")
                print()

def BuyNewLicence():

    # open LicenceFile for appending
    LicenceFile = open("LICENCE-KEYS.txt", "a")
    while True:
        LicenceType = input("Enter the type of licence (1 for single user, 3 for 3-user): ")
        if LicenceType not in ["1", "3"]:
            print("Invalid licence type selected!")
        else:
            break                   # valid licence type has been selected!
    Key = LicenceKey()
    if LicenceType == "1":          # single user licence
        Data = Key + " 1\n"
    else:                           # 3-user licence
        Data = Key + " 3 1\n"
    LicenceFile.write(Data)
    LicenceFile.close()

    # open LicenceFile for reading
    LicenceFile = open("LICENCE-KEYS.txt", "r")
    print(LicenceFile.read())
    LicenceFile.close()

def RegisterUser():
    # user to input 3-user licence key
    # test 1: licence key invalid
    # test 2: licence key valid, can register one more user
    # test 3: licence key valid, maximum number of users reached, cannot register
    
    # open LicenceFile for reading
    LicenceFile = open("LICENCE-KEYS.txt", "r")
    KeysArray = []
    for Line in LicenceFile:
        if Line[-1] == "\n":
            Line = Line[:-1]        # remove ending newline from line
        KeysArray.append(Line)
        print(Line)
    LicenceFile.close()

    Licence = input("Enter the 3-user licence to register a new user for: ")
    Found = False                   # does the licence key exist?
    for i in range(len(KeysArray)):
        if KeysArray[i][:10] == Licence:
            Found = True
            KeyIndex = i

    if Found == False:
        print("Licence key not found in your list!")
        return

    if KeysArray[KeyIndex][10:] == " 1":     # single-user licence
        print("Licence key found, but is a single-user licence, cannot register!")
        return
    else:
        UsersRegistered = int(KeysArray[KeyIndex][-1])
        if UsersRegistered == 3:
            print("Licence key valid, but maximum number of users reached, cannot register!")
        else:
            UsersRegistered += 1
            KeysArray[KeyIndex] = KeysArray[KeyIndex][:-1] + str(UsersRegistered)

            print("Success! A total of {0} users have now successfully registered for 3-user licence {1}."\
                  .format(UsersRegistered, KeysArray[KeyIndex][:10]))

            # recreate LICENCE-KEYS.txt file using KeysArray
            LicenceFile = open("LICENCE-KEYS.txt", "w")
            for Line in KeysArray:
                LicenceFile.write(Line + "\n")
            LicenceFile.close()

