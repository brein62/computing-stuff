def chatter(line):
    print("Chatterbox: " + line)

def bot_talk(text):
    print("Chatterbot: " + text)
    
def chatterbot(text_file):
    file = open(text_file, 'r')
    first_time = True           # first time saying hello?
    for line in file:
        if line[-1] == '\n':    # not the last line
            line = line[:-1]    # strip the newline if so
        chatter(line)           # talk to the bots
        if (('hello' in line.lower()) and (first_time == True)):
            bot_talk("Hi, how are you?")
            first_time = False
        elif 'hello' in line.lower():
            bot_talk("Hello again, welcome back!")
        elif ('thanks' in line.lower()) or ('thank you' in line.lower()):
            bot_talk("You are most welcome.")
        elif (line.lower().split()[0] == 'i') and (line.lower().split()[2].startswith('you')):
            love_verb = line.split()[1]
            bot_talk("You {0} me? I really {0} you too.".format(love_verb))
        else:
            bot_talk("Sorry, I do not understand...")
        print()                 # obligatory separatory newline

