from random import randint

def decoder():
    result = ""
    
    textfile = open("textstream.txt", "r")
    content = textfile.read().strip()
    numbersList = content.split(",")

    for i in range(len(numbersList)):
        numbersList[i] = int(numbersList[i])

    # modes can either be uppercase   (0),
    #                     lowercase   (1),
    #                  or punctuation (2)
    mode = 0

    for number in numbersList:
        
        # uppercase or lowercase mode
        if mode == 0 or mode == 1:

            lettersU = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lettersL = " abcdefghijklmnopqrstuvwxyz"
            
            letterIndex = number % 27

            # check if need to change mode
            if letterIndex == 0: 

                # switches the mode:
                # uppercase (0) --> lowercase   (1)
                # lowercase (1) --> punctuation (2)
                mode = mode + 1
            else:
                if mode == 0:   # uppercase
                    letter = lettersU[letterIndex]
                else:           # lowercase
                    letter = lettersL[letterIndex]

                result += letter

        # punctuation mode
        else:
            puncList = [
                None, "!", "?", ",", ".", " ",
                ";", '"', "'"
            ]
            
            puncIndex = number % 9

            # check if need to change mode
            if puncIndex == 0: 

                # switches the mode:
                # punctuation (2) --> uppercase (0)
                mode = 0
            else:
                punctuation = puncList[puncIndex]
                result += punctuation

    textfile.close()
    print(result)

def encoder():
    inputString = input("Enter the string to encode: ")
    resultArray = []

    # modes can either be uppercase   (0),
    #                     lowercase   (1),
    #                  or punctuation (2)
    currMode = 0
    prevMode = 0

    for character in inputString:

        # character is uppercase
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            currMode = 0

            # append 0s accordingly to change the
            # mode to UPPERCASE
            if prevMode == 1:
                resultArray.append(0)
                resultArray.append(0)
            elif prevMode == 2:
                resultArray.append(0)
    
            for i in range(len(alphabet)):
                if alphabet[i] == character:
                    resultArray.append(i)

        # character is lowercase
        elif character in "abcdefghijklmnopqrstuvwxyz":
            alphabet = " abcdefghijklmnopqrstuvwxyz"
            currMode = 1

            # append 0s accordingly to change the
            # mode to LOWERCASE
            if prevMode == 0:
                resultArray.append(0)
            elif prevMode == 2:
                resultArray.append(0)
                resultArray.append(0)

            for i in range(len(alphabet)):
                if alphabet[i] == character:
                    resultArray.append(i)

        # character is a punctuation
        else:
            punctuations = [
                None, "!", "?", ",", ".", " ",
                ";", '"', "'"
            ]
            currMode = 2

            # append 0s accordingly to change the
            # mode to PUNCTUATION
            if prevMode == 0:
                resultArray.append(0)
                resultArray.append(0)
            elif prevMode == 1:
                resultArray.append(0)

            for i in range(len(punctuations)):
                if punctuations[i] == character:
                    resultArray.append(i)

        # set currMode as new prevMode
        prevMode = currMode

    for i in range(len(resultArray)):
        resultArray[i] = str(resultArray[i])

    print(",".join(resultArray))

def encoder_random():
    inputString = input("Enter the string to encode: ")
    resultArray = []

    # modes can either be uppercase   (0),
    #                     lowercase   (1),
    #                  or punctuation (2)
    currMode = 0
    prevMode = 0

    for character in inputString:

        # character is uppercase
        if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            currMode = 0

            # append 0s accordingly to change the
            # mode to UPPERCASE
            if prevMode == 1:

                # mode: 1 (LOWERCASE)
                # (random multiple of 27)
                resultArray.append(27 * randint(0, 100))
                # mode: 2 (PUNCTUATION)
                # (random multiple of 9)
                resultArray.append(9 * randint(0, 300))
                # mode: 0 (UPPERCASE)
                
            elif prevMode == 2:
                
                # mode: 2 (PUNCTUATION)
                resultArray.append(9 * randint(0, 300))
                # mode: 0 (UPPERCASE)
                
            for i in range(len(alphabet)):
                if alphabet[i] == character:
                    resultArray.append(27 * randint(0, 100) + i)

        # character is lowercase
        elif character in "abcdefghijklmnopqrstuvwxyz":
            alphabet = " abcdefghijklmnopqrstuvwxyz"
            currMode = 1

            # append 0s accordingly to change the
            # mode to LOWERCASE
            if prevMode == 0:
                
                # mode: 0 (UPPERCASE)
                # (random multiple of 27)
                resultArray.append(27 * randint(0, 100))
                # mode: 1 (LOWERCASE)
                
            elif prevMode == 2:

                # mode: 2 (PUNCTUATION)
                # (random multiple of 9)
                resultArray.append(9 * randint(0, 300))
                # mode: 0 (UPPERCASE)
                # (random multiple of 27)
                resultArray.append(27 * randint(0, 100))
                # mode: 1 (LOWERCASE)
            
            for i in range(len(alphabet)):
                if alphabet[i] == character:
                    resultArray.append(27 * randint(0, 100) + i)
                    
        # character is a punctuation
        else:
            punctuations = [
                None, "!", "?", ",", ".", " ",
                ";", '"', "'"
            ]
            currMode = 2

            # append 0s accordingly to change the
            # mode to PUNCTUATION
            if prevMode == 0:
                
                # mode: 0 (UPPERCASE)
                # (random multiple of 27)
                resultArray.append(27 * randint(0, 100))
                # mode: 1 (LOWERCASE)
                # (random multiple of 27)
                resultArray.append(27 * randint(0, 100))
                # mode: 2 (PUNCTUATION)
                
            elif prevMode == 1:

                # mode: 1 (LOWERCASE)
                # (random multiple of 27)
                resultArray.append(27 * randint(0, 100))
                # mode: 2 (PUNCTUATION)

            for i in range(len(punctuations)):
                if punctuations[i] == character:
                    resultArray.append(9 * randint(0, 300) + i)
                    
        prevMode = currMode

    for i in range(len(resultArray)):
        resultArray[i] = str(resultArray[i])

    print(",".join(resultArray))
