def CalCheckDigit(Number, Total):
    Number = str(Number)
    Total  = int(Total)
    if len(Number) > 1:
        Digit = int(Number[0])
        Total += (Digit * (len(Number) + 1))
        NewNumber = Number[1:]
        CheckDigit = CalCheckDigit(NewNumber, Total)
    else:
        Digit = int(Number[0])
        Total += Digit * (len(Number) + 1)
        CalcModulus = Total % 11
        CheckValue = 11 - CalcModulus
        if CheckValue == 11:
            return str(0)
        else:
            if CheckValue == 10:
                return str("X")
            else:
                return str(CheckValue)
    if len(Number) == 9:
        return Number + CheckDigit
    else:
        return CheckDigit
    
ISBNFile = open("ISBNPRE.TXT", "r")
for line in ISBNFile:
    if line[-1] == "\n":
        line = line[:-1]
    print(CalCheckDigit(line, 0))
ISBNFile.close()
