import random
choices=["Rock","Paper","Scissors"]
computer=random.choice(choices)
player=False
cpu_score=0
player_score=0
while True:
    player=input("Rock,Paper or Scissors?").capitalize()  
    ##cpitalize() method returns a copy of original string and converts the first character of the string to a capital letter while making all the other characters in string lowercase letters
    ## Conditions of Rock,Paper and Scissors
    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="Paper":
            print("You lose!",computer,"covers",player)
            cpu_score+=1
        else:
            print("You win!",player,"covers",computer)
            player_score+=1
    elif player=="Paper":
        if computer=="Scissors":
            print("You lose!",computer,"cut",player)
            cpu_score+=1
        else:
            print("You win!",player,"covers",computer)
            player_score+=1
    elif player=="Scissors":
        if computer=="Rock":
            print("You lose...",computer,"smashes",player)
            cpu_score+=1
        else:
            print("You win!",player,"cut",computer)
            player_score+=1
    elif player=='End':
        print("Final Scores:")
        print(f"CPU:{cpu_score}")
        print(f"PLAYER:{player_score}")
        break

    
