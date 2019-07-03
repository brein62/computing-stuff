def ValidateUserID(ThisUserID):
    if len(ThisUserID) != 9:
        return 1
    if ThisUserID[:5] != "2015_":
        return 2
    if not ThisUserID[5:].isdigit():
        return 3
    return 0

def Task2():
    UserID = input("Enter an ID here: ")
    ValidationMessages = ["Valid User ID", "Invalid User ID - The User ID was not 9 characters", \
                          'Invalid User ID - The User ID does not start with "2015_"', \
                          'Invalid User ID - The User ID contains non-digit character']
    print(ValidationMessages[ValidateUserID(UserID)])

class PrintJob:
    def __init__(self, UserID, TerminalNo, 
