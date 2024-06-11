#my little guess game play work.
import random 
import os
import time
import sys

answer = random.randint(1, 20)

def loading()->None:
    print('Loading please wait',end="")
    for b in range (4):
        time.sleep(1)
        sys.stdout.write('.')
        sys.stdout.flush()
        
def clear_s() ->None:
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_msg():
   print("WELCOME TO AGB GUESS GAME🎯🎯😀")
   choice = input("1. Start game \n2. Exit\n\nENTER YOUR CHOICE:  ")
   if choice == "1":
       clear_s()
       game_on()
   elif choice == "2":
       clear_s()
       close()
       loading()
   else:
       clear_s()
       err_msg()
       
def err_msg():
      print("you have made an invalid selection, try again:\n\n")
      welcome_msg()
        
def close():
    print("GOODBYE!!! SEE YOU NEXT TIME😌\n")
    return 0
    
def game_on():
   reply= input("Are you ready to play???? \nENTER (y/n): ")
   if reply == 'y' or reply == 'Y' or reply == "yes" or reply == "Yes" or reply == "YES":
        clear_s()
        usr_name = input('Enter your name: ')
        clear_s()
        print("Hello! {}".format(usr_name))
        while True:
            level = input('\nSet difficulty level: \n1. Easy \n2. Hard\n\nEnter your choice: ')
            if level == '1':
                clear_s()
                print("Difficulty level set to 'Easy'\n LET ME GUESS A NUMBER \n")
                loading()
                clear_s()
            #loading()
                for attempts in range (8):
                    attempts = 8 - attempts
                    guess = int(input("you have {} attempt(s)\nGUEESS THE NUMBER: ".format(attempts)))
                    if attempts == 1:
                       clear_s()
                       print("Game over!! {}, YOU LOST❌❌\nCORRECT ANSWER : {}".format(usr_name, answer))
                       close()
                    elif guess == answer:
                       clear_s()
                       print("you are a smart genius!! {} 😀 that is CORRECT!\nCORRECT ANSWER IS {} ✅".format(usr_name, answer))
                       print("you WIN!!")
                       return 0
                    elif guess < answer:
                        clear_s()
                        print("HINT: your guess is lower  than the number😓 : try again")
                    else:
                        clear_s()
                        print("HINT: your guess is greater than the number😬 : try harder")
                    
                   
            elif level == '2':
                clear_s()
                print("Difficulty level set to 'Hard'\nLET ME GUESS A NUMBER\n")
                loading()
                clear_s()
                for attempts in range (4, -1, -1):
                    guess= int(input(f"you have {attempts} attempt(s)\nGUEESS A NUMBER: "))
                    if attempts == 1:
                        clear_s()
                        print("Game over {}, YOU LOST❌❌\nCORRECT ANSWER : {}".format(usr_name, answer))
                        return 0
                    
                    elif guess == answer:
                        clear_s()
                        print("you are a smart genius!! {} 😀 that is CORRECT!\nCORRECT ANSWER IS {}✅".format(usr_name, answer))
                        print("you WIN!!")
                        return 0
                    elif guess < answer:
                        clear_s()
                        print("HINT: your guess is lower  than the number😓 : try again")    
                    else:
                        clear_s()
                        print("HINT: your guess is greater than the number😬 : try harder")
            
            else:
                clear_s()
                print("invalid choice:")
            
   elif reply == 'n' or reply == 'N' or reply == "NO" or reply == "No" or reply == "no":
        clear_s()
        close()
        loading()
   else:
       clear_s()
       print("you have not made a valid option🌚")
       return game_on()
                 
loading()
clear_s()
welcome_msg()