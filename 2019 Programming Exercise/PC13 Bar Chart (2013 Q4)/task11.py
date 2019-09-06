# task 1.1

###     MAIN PROGRAM     ###
def main():
    freq_store = []         # store as array of tuples (x_value, freq)
    counter = 0             # counts number of X values
    while True:             # repeats until ZZZ is typed in
        x_value = input("Next X value ... <ZZZ to END> ")
        if x_value == "ZZZ":
            break           # exit out of loop and process
        if counter == 6:
            break           # exit out of loop and process
        # ask for frequency
        while True:
            freq = input("Frequency ... ")
            if freq.isdigit():               # is a number
                freq = int(freq)
                if freq >= 0 and freq <= 60: # within range
                    break                    # break out of loop
                else:
                    # print error message
                    print("Error: Frequency entered out of range [0, 60]")
                    print("Enter an integer between 0 and 60.")
                    print()
            else:
                    # print error message
                print("Error: Frequency entered not an integer.")
                print("Enter an integer between 0 and 60.")
                print()

        freq_store.append((x_value, freq))  # add to freq_store array
        counter += 1                        # increment counter

    ###   DATA PROCESSING   ###
    print()                             # heading
    print("+" * 30)
    print("Frequency distribution")
    print("+" * 30)

    for data_tuple in freq_store:
        x_value = data_tuple[0]
        freq    = data_tuple[1]
        print("  {0:<10}{1}".format(x_value, "@" * freq))
    
