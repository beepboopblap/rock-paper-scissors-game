import random as rdm 

choices = ["Rock", "Paper", "Scissors"]
ai_choice = rdm.choice(choices)

inp = input("Choose Rock, Paper or Scissors: ")


if inp not in choices:
    print("Not a choice!")

else:
    

    print("Computer chooses", ai_choice, "!")
    if ai_choice == "Rock":
        if inp == "Rock": 
            print("Draw!")
        elif inp == "Paper":
            print("You Lose")
        elif inp == "Scissors":
            print("You Win!")
    elif ai_choice == "Paper":
        if inp == "Rock":
            print("You Lose")
        elif inp == "Paper":
            print("Draw!")
        elif inp == "Scissors":
            print("You Win!")
    elif ai_choice == "Scissors":
        if inp == "Rock":
            print("You Win!")
        elif inp == "Paper":
            print("You Lose")
        elif inp == "Scissors":
            print("Draw!")

