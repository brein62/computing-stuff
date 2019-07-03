def IsPrime(N):
    flag = True
    for i in range(2, N):       # from 2 to N - 1, or always returns False
        if N % i == 0:          # i is a factor of N
            flag = False
            exit                # exits the for loop as flag is False
        else:                   # i is not a factor of N
            pass                # do nothing, flag remains the same
    if N == 1:
        flag = False            # 1 is not a prime number
    return flag

counter = 0                     # number of prime numbers between 1 and N
N = 0
while counter < 20:
    N += 1
    if IsPrime(N):              # N is prime
        print(N)
        counter += 1            # counter increments
