from random import *
file = open("NUMBERS.txt", "w")
s = ""
for i in range(100):
    s+=str(randint(1, 100)) + " "
file.write(s)
file.close()
