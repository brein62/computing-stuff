def main():
    n = input("Enter the value of n here: ")

    # note: validation is not needed

    n = int(n)

    # you need to check when n == 0
    if n == 0:
        print("Error: value doesn't exist.")
    else:
        total = 0

        # range(n) ranges from 0 to n - 1
        for i in range(n):
            total += (1 / (i + 1))

        print(total)
        
    print()
