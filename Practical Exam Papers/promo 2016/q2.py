def binary_recursive(array, input_value):
    element_found = False
    low_element = 0
    high_element = len(array) - 1
    index = int((low_element + high_element) / 2)
    if len(array) == 1:
        print(array)
        element_found = True
    else:
        if input_value < array[index]:      #if input is higher in alphabetical order than middle
            high_element = index            #left sub-array
            sub_array = array[low_element+1:high_element]
            binary_recursive(sub_array, input_value)
        else:                               #lower in alphabetical order than middle
            low_element = index + 1         #right sub-array
            sub_array = array[low_element:high_element+1]
            print(sub_array)
            binary_recursive(sub_array, input_value)
    if element_found == True:
        return array[index] + " is found in the array in position " + str(index + 1) + "."
    else:
        return "Not found"

def binary_search(array, input_value):          #array is the CITY array, input_value is the search key
    element_found = False
    low_element = 0
    high_element = len(array) - 1
    while (element_found != True) and (low_element <= high_element):
        index = int((low_element + high_element) / 2)
        if array[index] == input_value:
            element_found = True
        else:
            if input_value < array[index]:      #if input is higher in alphabetical order than middle
                high_element = index - 1        #left sub-array
            else:                               #lower in alphabetical order than middle
                low_element = index + 1         #right sub-array
    if element_found == True:
        return array[index] + " is found in the array in position " + str(index + 1) + "."
    else:
        return "Not found"

city_file = open("CITY.txt", "r")
city_array = []                                 #convert city file to list
for each_city in city_file:
    city_array.append(each_city[:-1])
city_file.close()

user_exited = False                             #checks if user has exited
while user_exited == False:
    city_input = input("Enter the city to search for: ")
    if city_input == "XXX":                      #'XXX' pressed!
        print("'XXX' pressed, exiting program.")
        user_exited = True
    else:                                       #keep on searching
        print(binary_search(city_array, city_input))
        print()
