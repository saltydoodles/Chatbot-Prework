from datetime import date
import time
import random

user_name = input("Hi there, what's your name? ")
time.sleep(0.5)
print(f"Nice to meet you, {user_name}!")
time.sleep(0.5)
user_age = int(input(f"Say, {user_name}, how old are you? "))
time.sleep(0.5)
if user_age == 17:
    print("Oh, that's my favorite number!")
    time.sleep(0.5)
elif 10 > user_age or user_age >= 100:
    print("Hm... I don't exactly believe you, but whatever.")
    time.sleep(0.5)
else:
    print("Oh, cool!")
    time.sleep(0.5)

print("Anyway, I can do some pretty neat stuff!")
time.sleep(0.5)


def chatbot_stuff():
    print("I can tell you the time.\nI can tell you the date.\nOr, we could play a game!")
    time.sleep(0.5)
    task_choice = input(f"So, what'll it be, {user_name}? ")
    time.sleep(0.5)

    if "TIME" in task_choice.upper():
        time_choice = True
    else:
        time_choice = False

    if "DATE" in task_choice.upper():
        date_choice = True
    else:
        date_choice = False

    if "PLAY" in task_choice.upper() or "GAME" in task_choice.upper():
        game_choice = True
    else:
        game_choice = False

    if time_choice == True:
        print("The time is " + time.strftime("%H:%M:%S", time.localtime()))
        time.sleep(0.5)

    if date_choice == True:
        print(f"The date is {date.today()}")
        time.sleep(0.5)

    if game_choice == True:
        def rerun():
                    go_again = input("Wanna go again? ")
                    if go_again.upper() == "YES":
                        play()
                    elif go_again.upper() == "NO":
                        print("Alrighty then!")
                    else:
                        print("Uh, could you repeat that?")
                        rerun()
        game = random.choice(["rps", "guess"])
        if game == "rps":
            def play():
                bot_choice = random.choice(["rock", "paper", "scissors"])
                print("Let's play Rock, Paper, Scissors!")
                time.sleep(0.5)
                print("Rock...")
                time.sleep(0.5)
                print("Paper...")
                time.sleep(0.5)
                print("Scissors...")
                time.sleep(0.5)
                rps_choice = input("SHOOT!!")
                if bot_choice == "rock":
                    if rps_choice.upper() == "ROCK":
                        print("Agh, a tie! Let's go again!")
                        time.sleep(0.5)
                        play()
                    elif rps_choice.upper() == "PAPER":
                        print("Ah, you got me!")
                        time.sleep(0.5)
                        rerun()
                    elif rps_choice.upper() == "SCISSORS":
                        print("Yay! I won!")
                        time.sleep(0.5)
                        rerun()
                    else:
                        print("Uh, what??")
                        time.sleep(0.5)
                        print("Let's try that again.")
                        time.sleep(0.5)
                        play()
                elif bot_choice == "paper":
                    if rps_choice.upper() == "PAPER":
                        print("Agh, a tie! Let's go again!")
                        time.sleep(0.5)
                        play()
                    elif rps_choice.upper() == "SCISSORS":
                        print("Ah, you got me!")
                        time.sleep(0.5)
                        rerun()
                    elif rps_choice.upper() == "ROCK":
                        print("Yay! I won!")
                        time.sleep(0.5)
                        rerun()
                    else:
                        print("Uh, what??")
                        time.sleep(0.5)
                        print("Let's try that again.")
                        time.sleep(0.5)
                        play()
                elif bot_choice == "scissors":
                    if rps_choice.upper() == "SCISSORS":
                        print("Agh, a tie! Let's go again!")
                        time.sleep(0.5)
                        play()
                    elif rps_choice.upper() == "ROCK":
                        print("Ah, you got me!")
                        time.sleep(0.5)
                        rerun()
                    elif rps_choice.upper() == "PAPER":
                        print("Yay! I won!")
                        time.sleep(0.5)
                        rerun()
                    else:
                        print("Uh, what??")
                        time.sleep(0.5)
                        print("Let's try that again.")
                        time.sleep(0.5)
                        play()
            play()
        elif game == "guess":
            def play():
                rand_num = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
                num_choice = int(input("I'm thinking of a number from 1 to 10, take a guess! "))
                time.sleep(0.5)
                if 1 > num_choice > 10:
                    print("Uh, that wasn't one of the numbers...")
                    time.sleep(0.5)
                    play()
                elif num_choice == rand_num:
                    print("You got it!")
                    time.sleep(0.5)
                    rerun()
                else:
                    print("Nope, that's not it!")
                    time.sleep(0.5)
                    rerun()
            play()
    def continue_check():
        keep_going = input("Need anything else? ")
        time.sleep(0.5)
        if keep_going.upper() == "YES":
            chatbot_stuff()
        elif keep_going.upper() == "NO":
            print("Alright, see you around then!")
            time.sleep(0.5)
        else:
            print("Sorry, could you repeat that?")
            time.sleep(0.5)
            continue_check()
    continue_check()

chatbot_stuff()
