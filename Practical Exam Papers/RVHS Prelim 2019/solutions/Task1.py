## TASK 1.1
def read_data(filename):
    file = open(filename, "r")
    output_array = []
    for line in file:
        if line[-1] == "\n":
            line = line[:-1]
        output_array.append(line.split(";"))
    return output_array

## TASK 1.2
def gender_count(cid_student_lst, is_female):
    count = 0
    if is_female == True:
        # count number of female students
        for record in cid_student_lst:
            if record[2] == "F":
                count += 1
    else:
        # count number of male students
        for record in cid_student_lst:
            if record[2] == "M":
                count += 1
    return count

## TASK 1.3
def role_statistics(cid_student_lst):
    role_frequency = {}
    for record in cid_student_lst:
        role = record[1]
        if role not in list(role_frequency.keys()):
            role_frequency[role] = 1
        else:
            role_frequency[role] += 1
    print("{0:<15}{1}".format("Role", "Number"))
    for each_role in role_frequency:
        freq = role_frequency[each_role]
        print("{0:<15}{1}".format(each_role, freq))
        
## TASK 1.4
import random
def form_random_group(cid_student_lst):
    
