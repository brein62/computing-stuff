# import randint() from random library
from random import randint

def decoder():
    # this will be the return string when
    # the decoder is run
    result = ""

    # opens the file to be read in Python
    textfile = open("textstream.txt", "r")

    # reads all the text content in the file,
    # then removes the ending newline using strip()
    content = textfile.read().strip()

    # numbersList contains all the numbers
    # in a list form, created using the
    # str.split(",") method
    numbersList = content.split(",")

    # converts every element of the numbersList
    # from string to integer using int()
    for i in range(len(numbersList)):
        numbersList[i] = int(numbersList[i])

    # modes can either be uppercase   (0),
    #                     lowercase   (1),
    #                  or punctuation (2)
    mode = 0        # default mode is (0)

    for number in numbersList:
        # uppercase or lowercase mode
        if mode == 0 or mode == 1:

            # index in this string represents 
            # the letter of the alphabet
            # (note the space at the front
            # as Python is 0-based and
            # A = 1, B = 2 etc.)
            lettersU = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            lettersL = " abcdefghijklmnopqrstuvwxyz"
            
            # index of the desired letter
            number = number % 27

            # check if need to change mode
            if number == 0: 

                # switches the mode:
                # uppercase (0) --> lowercase   (1)
                # lowercase (1) --> punctuation (2)
                mode = mode + 1
            else:
                if mode == 0:   # uppercase
                    letter = lettersU[number]
                else:           # lowercase
                    letter = lettersL[number]

                # add the letter to the return
                # string (result)
                result += letter

        # punctuation mode
        else:
            # index in this string represents 
            # the corresponding punctuation
            # (note the space at the front
            # as Python is 0-based and
            # ! = 1, ? = 2 etc.)
            punctuations = [
                None, "!", "?", ",", ".", " ",
                ";", '"', "'"
            ]
            
            # index of the desired punctuation
            number = number % 9

            # check if need to change mode
            if number == 0: 

                # switches the mode:
                # punctuation (2) --> uppercase (0)
                mode = 0
            else:
                punctuation = punctuations[number]

                # add the punctuation to the return
                # string (result)
                result += punctuation

    # don't forget to close the text file!
    textfile.close()

    # finally, print the return string, result.
    print(result)

def encoder():

    # get the user input string
    inputString = input("Enter the string to encode: ")

    # result array containing integers
    resultArray = []

    # modes can either be uppercase   (0),
    #                     lowercase   (1),
    #                  or punctuation (2)
    currMode = 0    # default mode is (0)
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

            # loop through every letter of
            # the alphabet
            for i in range(len(alphabet)):

                # alphabet[i] represents the
                # letter of the alphabet
                if alphabet[i] == character:

                    # append character index to array
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

            # loop through every letter of
            # the alphabet
            for i in range(len(alphabet)):

                # alphabet[i] represents the
                # letter of the alphabet
                if alphabet[i] == character:

                    # append character index to array
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

            # loop through every punctuation
            for i in range(len(punctuations)):

                # punctuations[i] represents
                # each punctuation
                if punctuations[i] == character:

                    # append punctuation index to array
                    resultArray.append(i)

        # set currMode as new prevMode
        prevMode = currMode

    # make every encoded number a string
    for i in range(len(resultArray)):
        resultArray[i] = str(resultArray[i])

    # join every character in resultArray
    # to form the result string, then print
    print(",".join(resultArray))

def encoder_random():

    # get the user input string
    inputString = input("Enter the string to encode: ")

    # result array containing integers
    resultArray = []

    # modes can either be uppercase   (0),
    #                     lowercase   (1),
    #                  or punctuation (2)
    currMode = 0    # default mode is (0)
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
                
            # loop through every letter of
            # the alphabet
            for i in range(len(alphabet)):

                # alphabet[i] represents the
                # letter of the alphabet
                if alphabet[i] == character:

                    # add multiple of 27 to character index
                    # then append character index to array
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

            # loop through every letter of
            # the alphabet
            for i in range(len(alphabet)):

                # alphabet[i] represents the
                # letter of the alphabet
                if alphabet[i] == character:

                    # add multiple of 27 to character index
                    # then append character index to array
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

            # loop through every punctuation
            for i in range(len(punctuations)):

                # punctuations[i] represents
                # each punctuation
                if punctuations[i] == character:

                    # add multiple of 9 to punctuation index
                    # then append punctuation index to array
                    resultArray.append(9 * randint(0, 300) + i)

        # set currMode as new prevMode
        prevMode = currMode

    # make every encoded number a string
    for i in range(len(resultArray)):
        resultArray[i] = str(resultArray[i])

    # join every character in resultArray
    # to form the result string, then print
    print(",".join(resultArray))
