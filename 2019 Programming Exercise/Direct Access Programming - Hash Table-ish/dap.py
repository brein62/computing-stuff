def HashAsia(CountryName):
    K = 0
    M = 47
    for character in CountryName:
        K += ord(character)
    A = K % M + 1
    return A
