# task 1.2

###     MAIN PROGRAM     ###
def main():
    freq_store = []         # store as array of tuples (x_value, freq)
    max_freq = 0            # maximum frequency (width: 80)
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
                
        if freq > max_freq:
            max_freq = freq                 # set maximum frequency
        
        freq_store.append((x_value, freq))  # add to freq_store array
        counter += 1                        # increment counter

    ###   DATA PROCESSING   ###
    print()                             # heading
    print("+" * 30)
    print("   Frequency distribution")
    print("+" * 30)
    print()

    for data_tuple in freq_store:
        x_value = data_tuple[0]
        freq    = data_tuple[1]
        
        # print five lines each (6 * (5 lines + 1 space) + 4 for heading = 40)
        print("    {0:<16}{1}".format("", chr(9608) * freq))
        print("    {0:<16}{1}".format("", chr(9608) * freq))
        print("    {0:<16}{1}".format(x_value, chr(9608) * freq))
        print("    {0:<16}{1}".format("", chr(9608) * freq))
        print("    {0:<16}{1}".format("", chr(9608) * freq))

        # chr(9608) is a shaded box character.

        # print newline to separate X values
        print()
    
