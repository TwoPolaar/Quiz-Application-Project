# Modules, variables, and functions:::

# Modules:::
from os.path import exists
import time
import os


#Variables:::

clear = lambda: os.system("clear")
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
load = ""
no_of_questions = ""

red = "\033[0;31m"
green = "\033[0;32m"
orange = "\033[0;33m"
blue = "\033[0;34m"
purple = "\033[0;35m"
cyan = "\033[0;36m"
White = "\033[0;37m" 
black = "\033[0;30m"
black = "\033[0;90m"
red = "\033[0;91m"
green = "\033[0;92m"
yellow = "\033[0;93m"
blue = "\033[0;94m"
magenta = "\033[0;95m"
cyan = "\033[0;96m"
white = "\033[0;97m"
cyan_back="\033[0;46m"
pink_back="\033[0;45m"
white_back="\033[0;47m"
blue_back="\033[0;44m"
orange_back="\033[0;43m"
green_back="\033[0;42m"
red_back="\033[0;41m"
grey_back="\033[0;40m"
bold = "\033[1m"
underline = "\033[4m"
italic = "\033[3m"
darken = "\033[2m"
reset = "\033[0m"


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
# System Text

def system_text(text):
    return (white + str(text) + cyan)        
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
# Makes user text
def user_text():
    return (cyan + str(input() + white))
    
#_________________________#
# Creates a new quiz


def create_quiz():
    global new_quiz
    global quiz_data

    #_________________________#
# Enables Playing Mode
def play_quiz():
    global making_quiz
    making_quiz = False

#_________________________# 
#Coloured Question

def qcolour(question):
    print(white + question)
    return input("" + cyan)

#_________________________# 
#Coloured Error

def error(text):
    return (red + text + cyan)
    
#_________________________#
#Asks the user question and stuff idk myself now

def quiz_play():
    clear()
    global bar
    global no_of_questions
    global quiz_data_temp
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
                time.sleep(1.5)
            else:
            
                print(red + "Incorrect")
                time.sleep(0.5)
                print("The correct answer was:", green + str(quiz_data_temp[counter] + red))
                time.sleep(1.5)
            clear()
            counter += 2
            if (counter - 1) == len(quiz_data_temp):
                break

        percentage = round((correct_ans / (len(quiz_data_temp) // 2) * 100), 2)

        print("\n")
        
        if percentage >= 50 and percentage < 80:
            print(white + "You achieved: ", yellow + str(percentage) + "%")
            print("(" + str(correct_ans) + "/" + (str(len(quiz_data_temp) // 2)) + ")")
        elif percentage >= 80:
            print(white + "You achieved: ", green + str(percentage) + "%")
            print("(" + str(correct_ans) + "/" + (str(len(quiz_data_temp) // 2)) + ")")
        elif percentage >= 35 and percentage < 50:
            print(white + "You achieved: ", orange + str(percentage) + "%")
            print("(" + str(correct_ans) + "/" + (str(len(quiz_data_temp) // 2)) + ")")
        elif percentage >= 0 and percentage < 34:
            print(white + "You achieved: ", red + str(percentage) + "%")
            print("(" + str(correct_ans) + "/" + (str(len(quiz_data_temp) // 2)) + ")")
    for i in range(1):
        play_quiz()
        print(white + "Enter Quiz Name:" + cyan)
        making_quiz_name = str(input())
        file_exists = exists(making_quiz_name + ".txt")
        
        if file_exists == False:
            clear()
            print(red + "Quiz does not exist")
            continue
        
        answer = making_quiz_name
        
        play(answer)
        clear()
        time.sleep(1.2)
        print(green + "Quiz Detected")
        time.sleep(1)
        print(white + "Starting Quiz:")
        time.sleep(3)
        clear()
        time.sleep(1)
        quiz_data_fetch()

#_________________________________________________#
# All the functionalities of making a quiz
def quiz_make():
    clear()
    global reset_line
    print(white + "Enter your Quiz name:" + cyan)    
    making_quiz_name = str(input() + ".txt")
    print()
    warning_ = red + (red + "!!! Do not stop the program while making the quiz. The quiz will not work!")
    time.sleep(0.4)
    print(warning_ + magenta)
    file_exists = exists(making_quiz_name)
    time.sleep(0.5)
    
    if file_exists == True:
        print(red + "This file has already been chosen." + cyan)
    else:
        quiz_name_local = open(making_quiz_name, "a+")
        for i in range(1 , 11):
            q = str(input( white + str(i) + ": Enter your question: " + cyan))
            time.sleep(0.5)
            ans = str(input(white + "Enter the answer: " + cyan))
            clear()
            quiz_name_local.write(str(q) + "\n")
            quiz_name_local.write(str(ans) + "\n")
            print(system_text("1. Exit"))
            print(system_text("2. Next Question"))
            print(error("3. Cancel Quiz"))
            user_input = str(input())
            if user_input == "1":
                if i >= 10:
                    clear()
                    time.sleep(0.5)
                    break
                else:
                    print(error("Your quiz must be at least 10 questions"))
                    time.sleep(2)
                    clear()
            elif user_input == "2":
                clear()
                continue
            elif user_input == "3":
                clear()
                time.sleep(2)
                break
            else:
                print(error("Invalid Response"))
                continue
        quiz_name_local.close
        clear()
        
# Actual Code

# Starting lines
print(bold + "QuizBase" + reset)
time.sleep(0.75)
while True:
    print()
    print(white +"1. Play a quiz")
    time.sleep(0.1)
    print("2. Make a quiz")
    answer = str(input("" + cyan))
    
    if answer == "1":
        quiz_play()
        print(green + "enter any key to go back")
        absolutely_pointless_variable = user_text()
        time.sleep(0.5)
        clear()
    elif answer == "2":
        quiz_make()
        print(green + "enter any key to go back")
        absolutely_pointless_variable = user_text()
        time.sleep(0.5)
        clear()
        
    else:
        error("Invalid Answer")
        clear()
        continue
        