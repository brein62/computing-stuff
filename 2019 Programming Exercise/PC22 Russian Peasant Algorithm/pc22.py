## TASK 1

# implement the Russian Peasant multiplication algorithm
def multiply():

    a = input("     Enter an integer: ")
    b = input("Enter another integer: ")
    # one or both is not an integer
    if str(a).isdigit() == False or str(b).isdigit() == False:
        print("One of the numbers input is not an integer.")
        return -1

    a = int(a)
    b = int(b)

    # sum of numbers (a) added in uncrossed rows
    total = 0
    while b >= 1:

        # odd value of b, include a in ToAdd
        if b % 2 != 0:
            total += a
            
        a *= 2
        b //= 2

    return total

print(multiply())

## TASK 2
class Stack:
    def __init__(self):
        self.__data = []

    def isempty(self):
        return (len(self.__data) == 0)

    def pop(self):
        if self.isempty():
            print("Stack is empty, cannot pop!")
            return -1
        else:
            return self.__data.pop(0)

    def push(self, newdata):
        self.__data = [newdata] + self.__data

    def top(self):
        if self.isempty():
            print("Stack is empty, cannot view top of stack!")
            return -1
        else:
            return self.__data[0]

def dectobin(decimal):
    opstack = Stack()
    output  = ""
    while decimal >= 1:
        opstack.push(decimal % 2)
        decimal //= 2
    while opstack.isempty() == False:
        output += str(opstack.top())
        opstack.pop()
    return output

## TASK 3
# a, b represent binary representations of a number
def binaryadd(a, b):
    # flip the two numbers to make them easier to process
    a = a[::-1]
    b = b[::-1]
    result = ""     # flipped result, returns actual result by flipping it back
    carry  = 0
    if len(a) < len(b):
        a, b = b, a
    if len(a) > len(b):
        for i in range(len(a)):
            if i < len(b):
                digit = int(a[i]) + int(b[i]) + carry
                if digit == 3:
                    result += "1"
                    carry  =  1
                elif digit == 2:
                    result += "0"
                    carry  =  1
                else:
                    result += str(digit)
                    carry  = 0
            else:
                digit = int(a[i]) + carry
                if digit == 2:
                    result += "0"
                    carry  =  1
                else: 
                    result += str(digit)
                    carry  =  0
        
        if carry == 1:
            result += "1"
    else:                           # equal length
        for i in range(len(a)):
            digit = int(a[i]) + int(b[i]) + carry
            if digit == 2:
                result += "0"
                carry  =  1
            else:
                result += str(digit)
                carry  = 0
        if carry == 1:
            result += "1"
    return result[::-1]
    

def multiplybin():
    

    a = input("     Enter an integer: ")
    b = input("Enter another integer: ")
    # one or both is not an integer
    if str(a).isdigit() == False or str(b).isdigit() == False:
        print("One of the numbers input is not an integer.")
        return -1

    a = dectobin(int(a))
    b = dectobin(int(b))

    # list of binary numbers (a) added in uncrossed rows
    binlist = []
    while len(b) >= 1:

        # odd value of b, include a in ToAdd
        if b[-1] != "0":
            binlist.append(a)
            
        a += "0"
        b  = b[:-1]

    bintotal = "0"
    for binaryno in binlist:
        bintotal = binaryadd(bintotal, binaryno)
        
    print(bintotal)
    print(binlist)
