def Converter(DenaryNumber):
    if DenaryNumber == 0 or DenaryNumber == 1:
        print(DenaryNumber)
    else:
        print(DenaryNumber % 2, end = "")
        Converter(int(DenaryNumber / 2))

Converter(56)

### Error: The output it produces would be flipped. To fix this, swap the 2 lines as shown below:
def ConverterFixed(DenaryNumber):
    if DenaryNumber == 0 or DenaryNumber == 1:
        print(DenaryNumber)
    else:
        ConverterFixed(int(DenaryNumber / 2))
        print(DenaryNumber % 2, end = "")

ConverterFixed(56)
ConverterFixed(28)
