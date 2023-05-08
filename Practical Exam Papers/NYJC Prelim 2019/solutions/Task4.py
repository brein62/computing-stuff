## TASK 4.1
def Cipher(NewAlphabet, Key):
    ChosenLetters = []
    for letter in Key:
        if letter not in ChosenLetters:
            ChosenLetters.append(letter)

    for letter in ChosenLetters:
        NewAlphabet.remove(letter)

    NewAlphabet = ChosenLetters + NewAlphabet

    return NewAlphabet

## TASK 4.2
def Task42():
    Alphabet = [chr(65 + i) for i in range(26)]
    Key = ""
    while not Key.isalpha():
        Key = input("Enter a key here: ")
        if not Key.isalpha():
            print("The key must contain only letters.")
            print()

    Key = Key.upper()
    CipherAlphabet = Cipher(Alphabet, Key)
    print(" ".join(CipherAlphabet))
    print()

## TASK 4.4

# returns alphabet position:
# A -> 0, B -> 1, C -> 2, ... , Z -> 25
# This represents the address of the cipher message.
def AlphaPos(letter):
    letter = letter.upper()
    return ord(letter) - 65

def DisplayMenu():
    print("1. Encode a message")
    print("2. Decode a message")
    print("3. -1 to Quit")

def Encode():
    Alphabet = [chr(65 + i) for i in range(26)]
    Key     = ""
    Message = ""
    while not Key.isalpha():
        Key = input("Enter a key here: ")
        if not Key.isalpha():
            print("The key must contain only letters.")
            print()

    CipherAlphabet = Cipher(Alphabet, Key)
    CipherMessage  = ""

    Message = input("Enter a message here: ")
    for letter in Message:
        if letter.isalpha():
            letter = letter.upper()
            position = AlphaPos(letter)
            CipherMessage += CipherAlphabet[position]
        else:
            CipherMessage += letter

    print("Encoded message:", CipherMessage)

# find position of letter in cipher array
def PositionOf(CipherArray, letter):
    letter = letter.upper()
    for i in range(len(CipherArray)):
        if letter == CipherArray[i].upper():
            return i

def Decode():
    Alphabet = [chr(65 + i) for i in range(26)]
    Key     = ""
    Message = ""
    while not Key.isalpha():
        Key = input("Enter a key here: ")
        if not Key.isalpha():
            print("The key must contain only letters.")
            print()

    CipherAlphabet = Cipher(Alphabet, Key)
    CipherMessage  = ""

    Message = input("Enter a message here: ")
    for letter in Message:
        if letter.isalpha():
            letter = letter.upper()
            position = PositionOf(CipherAlphabet, letter)
            CipherMessage += chr(65 + position)
        else:
            CipherMessage += letter

    print("Decoded message:", CipherMessage)

def Task44():
    Alphabet = [chr(65 + i) for i in range(26)]
    option   = ""
    while option != "3":
        DisplayMenu()
        option = input("Enter an option here: ")
        if option == "1":
            Encode()
        elif option == "2":
            Decode()
        elif option != "3":
            print("The option you have entered is invalid.")

## TASK 4.5
Alphabet = [chr(65 + i) for i in range(26)]
InterceptFile = open("INTERCEPT.txt", "r")
CharacterDict = {}
for letter in Alphabet:
    CharacterDict[letter] = 0
for line in InterceptFile:
    if line[-1] == "\n":
        line = line[:-1]
    for letter in line:
        if letter.isalpha():
            CharacterDict[letter] += 1
InterceptFile.close()

SortedAlphabet = Alphabet
# perform bubble sort such that most frequent letter is at the start
for i in range(len(SortedAlphabet)):
    for j in range(len(SortedAlphabet) - 1):
        if CharacterDict[SortedAlphabet[j]] < CharacterDict[SortedAlphabet[j + 1]]:
            temp = SortedAlphabet[j]
            SortedAlphabet[j] = SortedAlphabet[j + 1]
            SortedAlphabet[j + 1] = temp
    

output = "{0:<20}".format("Ciphertext Letter:")
for letter in SortedAlphabet:
    output += "{0:<4}".format(letter)
output += "\n"
output += "{0:<20}".format("Frequency:")
for letter in SortedAlphabet:
    output += "{0:<4}".format(CharacterDict[letter])
print(output)

