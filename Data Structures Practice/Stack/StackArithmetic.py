class ListNode:
    def __init__(self, Data, Pointer):
        self.__Data = Data
        self.__Pointer = Pointer

    def SetData(self, NewData):
        self.__Data = NewData

    def SetPointer(self, NewPointer):
        self.__Pointer = NewPointer

    def GetData(self):
        return self.__Data

    def GetPointer(self):
        return self.__Pointer

class Stack:
    def __init__(self):
        self.__Start = None
        self.__Size = 0

    def IsEmpty(self):
        return (self.__Start == None)

    def __str__(self):
        output = ""
        if self.IsEmpty():
            output = "Stack is empty."
        else:
            output = "Number of elements in stack: " + str(self.__Size) + "\n"
            output += "-" * 42 + "\n"
            output += "|{0:^40}|\n".format("STACK")
            output += "-" * 42 + "\n"
            curr = self.__Start
            while curr != None:
                output += "|{0:^40}|\n".format(curr.GetData())
                curr = curr.GetPointer()
            output += "-" * 42 + "\n"

        return output

    def Push(self, Data):                                   # add to front
        NewNode = ListNode(Data, self.__Start)              # self.__Start: node after this new node
        self.__Start = NewNode
        self.__Size += 1

    def Pop(self):                                          # remove from front
        if self.IsEmpty():
            print("Stack is empty, cannot pop.")
            return None
        else:
            Top = self.Top()
            self.__Start = self.__Start.GetPointer()
            self.__Size -= 1
            return Top

    def Top(self):
        if self.IsEmpty():
            return None
        else:
            return self.__Start.GetData()

    def Size(self):
        return self.__Size

def InfixToPostfix(InfixExpression):        # separated by space ( A + B ) * 16 - ( C / D ) for eg
    '''Returns a string representing an expression in a postfix notation.'''
    InfixExpression     += ' )'
    TokenList           =  InfixExpression.split()  
    OpStack             =  Stack()
    PostfixList         =  []
    Precedence          =  { "*": 2, "/": 2, \
                             "+": 1, "-": 1  }
    OpStack.Push('(')
    for Token in TokenList:
        if Token == '(':                    # Step 2b
            OpStack.Push('(')
        elif Token == ')':                  # Step 2d
            while OpStack.Top() != '(':
                PostfixList.append(OpStack.Pop())
            if OpStack.Top() == '(':
                OpStack.Pop()
        elif Token in "+-*/":               # Step 2c
            while OpStack.Top() in "+-*/" and Precedence[Token] <= Precedence[OpStack.Top()]:
                PostfixList.append(OpStack.Pop())
            OpStack.Push(Token)
        else:                               # Step 2a
            PostfixList.append(Token)
    return " ".join(PostfixList)

def EvaluateExpression(x, y, op):
    if op == "+":
        return x + y
    elif op == "-":
        return x - y
    elif op == "*":
        return x * y
    else:
        return x / y
    

def EvaluatePostfix(PostfixExpression):
    '''Evaluates an expression in a postfix notation.'''
    OpStack              = Stack()
    PostfixList          = PostfixExpression.split()
    for Token in PostfixList:
        if Token in "+-*/":
            y = float(OpStack.Pop())
            x = float(OpStack.Pop())
            if (int(x) == x): x = int(x)
            if (int(y) == y): y = int(y)
            OpStack.Push(EvaluateExpression(x, y, Token))
        else:
            OpStack.Push(Token)
    return OpStack.Top()
            
    
    
    

# test equations
print("-" * 73)
print("|{0:^30}|{1:^30}|{2:^10}|".format("Original", "Postfix", "Result"))
print("-" * 73)
print("|{0:^30}|{1:^30}|{2:^10}|".format("5 * ( 6 + 2 ) - 12 / 4", InfixToPostfix("5 * ( 6 + 2 ) - 12 / 4"), EvaluatePostfix(InfixToPostfix("5 * ( 6 + 2 ) - 12 / 4"))))
print("|{0:^30}|{1:^30}|{2:^10}|".format("( 6 + 2 ) * 5 - 8 / 4", InfixToPostfix("( 6 + 2 ) * 5 - 8 / 4"), EvaluatePostfix(InfixToPostfix("( 6 + 2 ) * 5 - 8 / 4"))))
print("-" * 73)
