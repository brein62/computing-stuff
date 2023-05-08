## TASK 1
def Task1():
    count = 0           # total number of names successfully input
    name_array = []     # array storing tuples of (name, steps)
    while count < 10:

        name_valid = False
        while not name_valid:
            name  = input("Enter the name here (XXX to quit): ")

            # perform validation on name
            if name == "":      # name is empty string
                print("Name cannot be empty!")
                print()
            elif "," in name:   # name contains comma
                print("Name cannot contain a comma!")
                print()
            else:
                name_valid = True

        if name == "XXX":       # exit
            break

        steps_valid = False
        while not steps_valid:
            steps = input("Enter the number of steps here:    ")

            # perform validation on steps
            if not steps.isdigit():                     # are all the characters digits?
                print("The number of steps is not an integer!")
                print()
            else:
                steps = int(steps)
                if steps < 0 or steps > 100000:     # is the number of steps in range?
                    print("The number of steps is out of range! Type a number between 0 and 100000.")
                    print()
                else:
                    steps_valid = True
                    print()

        # both name and steps are valid!
        name_array.append((name, steps))
        count += 1

    highest_steps = ("", -1)     # (name, steps) tuple with highest number of steps
    for pair in name_array:
        if pair[1] > highest_steps[1]:
            highest_steps = pair

    star_file = open("STAR.txt", "r")
    last_week_data = star_file.read()
    last_week_name, last_week_steps = last_week_data.split(",")
    star_file.close()
    print("Last week,", last_week_name, "was 'Star of the Week' with", last_week_steps, "steps taken.")

    this_week_name, this_week_steps = highest_steps
    print("This week,", this_week_name, "is 'Star of the Week' with", this_week_steps, "steps taken.")

    # update STAR.txt
    star_file = open("STAR.txt", "w")
    star_file.write(this_week_name + "," + str(this_week_steps))
    star_file.close()
    
Task1()