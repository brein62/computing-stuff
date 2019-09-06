# task 1.3

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
            if freq.isdigit():              # is a number
                freq = int(freq)
                if freq >= 0:               # within range
                    break                   # break out of loop
                else:
                    # print error message
                    print("Error: Frequency entered must be 0 or a positive integer.")
                    print()
            else:
                # print error message
                print("Error: Frequency entered must be 0 or a positive integer.")
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
    
    # 60 = 80 total - 20 used for labelling at the start of the line
    # scaling will only be used if max_freq > 60.
    if max_freq > 60:
        freq_scale = 60 / max_freq
    else:
        freq_scale = 1              # normal scale

    for data_tuple in freq_store:
        x_value = data_tuple[0]
        freq    = data_tuple[1]
        
        # print five lines each (6 × (5 lines + 1 space) + 4 for heading = 40)
        print("    {0:<16}{1}".format("", chr(9608) * round(freq * freq_scale)))
        print("    {0:<16}{1}".format("", chr(9608) * round(freq * freq_scale)))
        print("    {0:<16}{1}".format(x_value, chr(9608) * round(freq * freq_scale)))
        print("    {0:<16}{1}".format("", chr(9608) * round(freq * freq_scale)))
        print("    {0:<16}{1}".format("", chr(9608) * round(freq * freq_scale)))

        # chr(9608) is a shaded box character.

        # print newline to separate X values
        print()

    # print horizontal axis
    print("{0:<19}|{1}".format("", "---------|" * 6))

    h_labels = "{0:16}".format("")  # a string containing labels

    # if scaling is required
    if max_freq > 60:
        for i in range(7):          # from 0 to 6 inclusive
            h_labels += "{0:>6.2f}{1:<4}".format(max_freq * i / 6, "")
    else:
        for i in range(7):          # from 0 to 6 inclusive
            h_labels += "{0:>6.2f}{1:<4}".format(60 * i / 6, "")

    print(h_labels)
