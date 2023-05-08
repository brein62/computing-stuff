def InsertionSort(array, last):
    if last <= 1:
        return
    else:
        InsertionSort(array, last - 1)
        LastElement = array[last - 1]
        j = last - 2

        while (j >= 0 and array[j] >= LastElement):
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = LastElement

def InsertionSortModified(array, last):
    if last <= 1:
        return
    else:
        InsertionSortModified(array, last - 1)
        LastElement = array[last - 1]
        j = last - 2

        while (j >= 0 and array[j] >= LastElement):
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = LastElement
        print("Element at position", last, "is being inserted in position", j + 2)

countriesfile = open("COUNTRIES.txt", "r")
countries     = []      # array containing all the countries
for country in countriesfile:
    if country[-1] == "\n":
        country = country[:-1]
    countries.append(country)
countriesfile.close()
print(countries)
InsertionSortModified(countries, len(countries))
print(countries)
