## TASK 4.1
def integral_image():
    InputFile = open("IMAGE1.IN", "r")
    OriginalArray = []      # array containing original pixel values
    for line in InputFile:
        if line[-1] == "\n":
            line = line[:-1]
        LineArray = line.split(" ")
        NewLineArray = []   # LineArray with blank chars removed
        for entry in LineArray:
            if entry != '':
                NewLineArray.append(int(entry))
        OriginalArray.append(NewLineArray)
    print(OriginalArray)

    IntegralImageArray = [[0 for i in range(len(OriginalArray))\
                           ] for j in range(len(OriginalArray))]
    for i in range(len(IntegralImageArray)):
        for j in range(len(IntegralImageArray)):
            # from 0 to i
            for k in range(i + 1):
                # from 0 to j
                for l in range(j + 1):
                    IntegralImageArray[i][j] += OriginalArray[k][l]
                    
    InputFile.close()
    OutputFile = open("IMAGE1.OUT", "w")
    for i in range(len(IntegralImageArray)):
        for j in range(len(IntegralImageArray)):
            OutputFile.write("{0:<5}".format(IntegralImageArray[i][j]))
        OutputFile.write("\n")
    OutputFile.close()

    # output value of D - B - C + A
    D = IntegralImageArray[3][3]
    B = IntegralImageArray[1][3]
    C = IntegralImageArray[3][1]
    A = IntegralImageArray[1][1]
    print("Value of D - B - C + A =", D - B - C + A)

## TASK 4.2
import random
# This function generates a m * n array and saves
# it into IMAGE2.IN.
def GenerateRandomArrayFile(m = 12, n = 8):
    OriginalArray = [[0 for i in range(n)\
                      ] for j in range(m)]
    for i in range(m):
        for j in range(n):
            OriginalArray[i][j] = random.randint(0, 20)

    OutputFile = open("IMAGE2.IN", "w")
    for i in range(m):
        for j in range(n):
            OutputFile.write("{0:<5}".format(OriginalArray[i][j]))
        OutputFile.write("\n")
    OutputFile.close()
            
    
def magic(m = 12, n = 8):
    GenerateRandomArrayFile(m, n)
    InputFile = open("IMAGE2.IN", "r")
    OriginalArray = []      # array containing original pixel values
    for line in InputFile:
        if line[-1] == "\n":
            line = line[:-1]
        LineArray = line.split(" ")
        NewLineArray = []   # LineArray with blank chars removed
        for entry in LineArray:
            if entry != '':
                NewLineArray.append(int(entry))
        OriginalArray.append(NewLineArray)
    print(OriginalArray)

    IntegralImageArray = [[0 for i in range(n)\
                           ] for j in range(m)]
    for i in range(m):
        for j in range(n):
            # from 0 to i
            for k in range(i + 1):
                # from 0 to j
                for l in range(j + 1):
                    IntegralImageArray[i][j] += OriginalArray[k][l]
                    
    InputFile.close()
    OutputFile = open("IMAGE2.OUT", "w")
    for i in range(m):
        for j in range(n):
            OutputFile.write("{0:<5}".format(IntegralImageArray[i][j]))
        OutputFile.write("\n")
    OutputFile.close()

    LeftX   = int(input("  Enter the left index of the rectangle: "))
    RightX  = int(input(" Enter the right index of the rectangle: "))
    TopY    = int(input("   Enter the top index of the rectangle: "))
    BottomY = int(input("Enter the bottom index of the rectangle: "))

    # output value of D - B - C + A
    D = IntegralImageArray[RightX][BottomY]
    B = IntegralImageArray[LeftX][BottomY]
    C = IntegralImageArray[RightX][TopY]
    A = IntegralImageArray[LeftX][TopY]
    print("Value of D - B - C + A =", D - B - C + A)

integral_image()
