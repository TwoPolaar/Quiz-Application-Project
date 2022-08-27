# Modules, variables, and functions:::

# Modules:::
from os.path import exists


#Variables:::

making_quiz = True
playing_quiz = True
quiz_data = {}
new_quiz = ""
quiz = ""
quiz_len = []
start_quiz = False
quiz_data_temp = []
correct_ans = 0
quiz_name = ""
making_quiz_name = ""

bright_white = "\u001b[37;1m"
black = "\u001b[30m"
red = "\u001b[31;1m"
green = "\u001b[32;1m"
white = "\u001b[37m"
cyan = "\u001b[36m"
magenta = "\u001b[35m"
bright_red = "\u001b[31;1m"
bold = "\u001b[1m"

# Functions:::

# Enables "Make Quiz" mode


def make_quiz():
    global making_quiz
    global playing_quiz

    playing_quiz = False
    making_quiz = True
    print(making_quiz)
    print(playing_quiz)


#_________________________#
# Enables "Play Quiz" mode


def play_quiz():
    global making_quiz
    global playing_quiz
    print(playing_quiz)

    playing_quiz = True
    making_quiz = False
    print(playing_quiz)
#_________________________#
# Creates a new quiz


def create_quiz(name):
    global new_quiz
    global quiz_data
    new_quiz = name
    print("Error indicates an unoriginal name.")
    quiz_data = open(str(name), "x")


#_________________________#
# Creates a new question.
def create_question(question, answer):
    print = ""


#_________________________#
# Enables Playing Mode
def play_quiz():
    global making_quiz
    making_quiz = False

#_________________________# 
#Coloured Question

def qcolour(question):
    print(bright_white + question)
    return input("" + cyan)
#_________________________#
#Asks the user question and stuff idk myself now

def quiz_play():

    def play(quiz_name):
        global playing_quiz
        global quiz
        global quiz_len
        global start_quiz
        global quiz_data_temp
        if playing_quiz == True:
            quiz_open = open(str(quiz_name) + ".txt", "r")
            quiz_data_ini = quiz_open.readlines()
            quiz_data_temp = []
            
            for item in quiz_data_ini:
                quiz_data_temp.append(item.rstrip())
            
            
            quiz_len = len(quiz_data_temp)
            count = 1
            
            while True:
                global quiz_data
            
                quiz_data[quiz_data_temp[count - 1]] = quiz_data_temp[count]
                
                if count == (quiz_len - 1):
                    start_quiz = True
                    break
                
                count += 2
    
    
    def quiz_data_fetch():
        global correct_ans 
        global quiz_data_temp
        global quiz_data
        counter = 1
        while True:
            answer = ""
                
            answer = qcolour(quiz_data_temp[counter - 1])
            
            if answer.lower() == str(quiz_data_temp[counter]):
            
                print(green + "Correct" + cyan)
                correct_ans += 1
            
            else:
            
                print(red + "Incorrect" + cyan)
            
            
            counter += 2
            if (counter - 1) == len(quiz_data_temp):
                break
    
    
    for i in range(1):
        play_quiz()
        print(magenta + "Enter Quiz Name:" + cyan)
        making_quiz_name = str(input())
        file_exists = exists(making_quiz_name + ".txt")
        if file_exists == False:
            print(red + "Quiz does not exist")
            continue
        answer = making_quiz_name
        play(answer)
        print(bright_white + "\n"
             "Starting Quiz:")
        quiz_data_fetch()

#_________________________________________________#
# All the functionalities of making a quiz
def make_quiz():
    print(magenta + "Enter your Quiz name:" + cyan) 
    
    making_quiz_name = str(input())
    
    file_exists = exists(making_quiz_name)
    
    if file_exists == True:
        print(red + "This file has already been chosen." + cyan)
    else:
        

# Actual Code

# Starting lines
print(bright_white +":::Quizwork:::")
print("\n")
print(magenta +"1. Play a quiz\n"
     "2. Make a quiz (Under development!!!)")
answer = str(input("" + cyan))

if answer == "1":
    quiz_play()

#Quiz Making
if making_quiz == True:
    print(magenta + "Enter your Quiz name:" + cyan) 
    making_quiz_name = str(input())
    file_exists = exists(making_quiz_name)
    if file_exists == True:
        print(red + "This file has already been chosen." + cyan)
        