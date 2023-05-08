# returns the difference between two numbers
def diff(a, b):
    if a > b:
        return a - b
    else:
        return b - a

import random
frequency = [0 for i in range(20+1)]
for i in range(1000):
    integer = random.randint(1, 20)
    frequency[integer] += 1

expected = int(1000/20)
print("Expected frequency:", expected)
print("{0:<10}{1:<10}{2:<20}".format("Integer:", "Frequency", "Difference from expected"))
for i in range(1,20+1):
    print("{0:<10}{1:<10}{2:<20}".format(i, frequency[i], diff(frequency[i], expected)))
