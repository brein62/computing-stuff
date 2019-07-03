def punc_decoder(i):
    punc_array = ['!', '?', ',', '.', ' ', ';', '"', '\'']
    return punc_array[i - 1]

def char_mode(c):
    punc_array = ['!', '?', ',', '.', ' ', ';', '"', '\'']
    if ord(c) >= 65 and ord(c) <= 90:   #uppercase
        mode = 0
    elif ord(c) >= 97 and ord(c) <= 122:
        mode = 1
    else:
        mode = 2
    return mode

def punc_encode(i):
    punc_array = ['!', '?', ',', '.', ' ', ';', '"', '\'']
    for j in range(len(punc_array)):
        if i == punc_array[j]:
            return "," + str(j + 1)
            break                       # O(n) anyway jfkshfuiwehfuhweuif

def decoder():
    text_file = open("textstream.txt", "r")
    for line in text_file:
        contents = line
    numarray = contents.split(',')
    mode = 0                            # 0: upper, 1: lower, 2: punct
    result = ""
    for i in numarray:
        i = int(i)                      # god i love python
        if mode == 0:
            new_i = i % 27
            if new_i == 0:
                mode += 1
            else:
                result += chr(64 + new_i)
        elif mode == 1:
            new_i = i % 27
            if new_i == 0:
                mode += 1
            else:
                result += chr(96 + new_i)
        else:
            new_i = i % 9
            if new_i == 0:
                mode = 0
            else:
                result += punc_decoder(new_i)
    print(result)

def encode_mode(character, mode):
    if mode == 0:
        i = ord(character) - 64
        return "," + str(i)
    elif mode == 1:
        i = ord(character) - 96
        return "," + str(i)
    elif mode == 2:
        return punc_encode(character)
    else:
        i = ord(character) - 64
        return str(i)
        

def encoder():
    s = input("Enter a sentence: ")
    prev_mode = 0
    mode = 0
    encoded = encode_mode(s[0], 3)
    for character in s[1:]:
        mode = char_mode(character)
        # if prev in different mode
        if mode != prev_mode:
            difference = ((mode - prev_mode) + 3) % 3
            encoded += (",0" * difference)
            encoded += encode_mode(character, mode)
        else:
            encoded += encode_mode(character, mode)
        prev_mode = mode
    print(encoded)
            
