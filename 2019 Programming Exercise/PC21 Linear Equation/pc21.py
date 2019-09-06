eq_file = open("equation.txt", "r")
eq_text = eq_file.read().strip()
eq_text += "="          # to signify end of equation

coefficient = 0
constant    = 0
LHS         = True
term        = ""        # holds the string representation of a term.
terms       = []        # holds all the terms present
negative    = False     # is the next term negative?
letter      = ""
def append_term():
    if negative:
        if LHS:
            terms.append("-" + term)
        else:
            terms.append(term)
    else:
        if LHS:
            terms.append(term)
        else:
            terms.append("-" + term)
for char in eq_text:
    if char == "+" or char == "=":
        append_term()
        negative = False
        term = ""
    elif char == "-":
        append_term()
        negative = True
        term = ""
    else:
        term += char
    if char == "=":
        LHS = False
for eachterm in terms:
    if eachterm[-1].isalpha():
        letter = eachterm[-1]
        if len(eachterm) == 1:                              # singular x term
            coefficient += 1
        elif (len(eachterm) == 2 and eachterm[0] == "-"):   # -x term
            coefficient -= 1
        else:
            coefficient += int(eachterm[:-1])
    else:
        constant += int(eachterm)

# not needed in qn, just for fun
if constant >= 0:
    print("Equation to solve: {}{} + {} = 0".format(coefficient if coefficient != 1 else "", letter, constant))
else:
    print("Equation to solve: {}{} - {} = 0".format(coefficient if coefficient != 1 else "", letter, -constant))

print("{} = {:.3f}".format(letter, -constant/coefficient))
