## TASK 2.1
SGQRFile = open("SGQR.TXT", "r")
SGQRText = SGQRFile.read()
SGQRFile.close()

index   = 0       # index of character in SGQRText as it is processed
records = []
# loops for every record
while index < len(SGQRText):
    record = SGQRText[index:index + 4]
    index += 4
    length = int(SGQRText[index - 2:index])
    index += length
    record += SGQRText[index - length:index]
    records.append(record)

# print last record
print(records[-1])

## TASK 2.2
def hex2oct(hexa):
    Hex2BinDict = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", \
                   "4": "0100", "5": "0101", "6": "0110", "7": "0111", \
                   "8": "1000", "9": "1001", "A": "1010", "B": "1011", \
                   "C": "1100", "D": "1101", "E": "1110", "F": "1111"}

    binary = ""
    for hexdigit in hexa:
        binary += Hex2BinDict[hexdigit]

    # ensure binary representation has a multiple of 3 digits
    while len(binary) % 3 != 0:
        binary = "0" + binary

    print(binary)
    Bin2OctDict = {"000": "0" , "001": "1" , "010": "2" , "011": "3" , \
                   "100": "4" , "101": "5" , "110": "6" , "111": "7" }

    octal = ""
    for i in range(len(binary) // 3):
        threebits = binary[3 * i: 3 * i + 3]
        octal += Bin2OctDict[threebits]

    return octal

print(hex2oct("4F63A"))

## TASK 2.3
def ValidateHex(hexa):
    validchars = ["0", "1", "2", "3", "4", "5", "6", "7",\
                  "8", "9", "A", "B", "C", "D", "E", "F"]
    hexa = hexa.upper()
    valid = True
    for digit in hexa:
        if digit not in validchars:
            valid = False
            break
    return valid

print(ValidateHex("4F63A")) # True
print(ValidateHex("4ff54")) # True
print(ValidateHex("weird")) # False
