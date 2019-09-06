def main():
    x = input("Enter an integer from 10 to 20 (exclusive): ")
    x = int(x)
    if x <= 10 or x >= 20:
        print("The number, " + str(x) + ", is out of range.")
    else:
        print(x + 1, x, x - 1)
    print()
