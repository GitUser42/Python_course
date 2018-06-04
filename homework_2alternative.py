#alternative rock paper scissors
from random import randint
t=["rock","paper","scissors"] #list mit den Spieloptionen
computer=t[randint(0,2)] # der pc darf aus der Liste t die 0-2 Stelle benutzen. (lists starten bei Stelle 0)

player=False # Der player wird False gesetzt da er am Ende eine Variable zugeordnet kriegt und demnach true gesetzt wird

loser = "Dear player, I´m dissapointed you just lost the match against this stupid pc. I hope you learned your lesson!"

while player == False:
    player=input(" Choose your fighter!: rock, paper or scissors?") 
    if player == computer:
        print("Tied Game!","You both used", computer) # egal ob man computer oder player eingibt, beide haben ja das selbe 
    elif player == "rock":
        if computer == "paper":
            print(loser,"Computer played:",computer,"You played:",player)  # wie setzte ich einen Zeilenumbruch ein
        else:
            print("You win!","Computer played:",computer,"You played:",player)
    elif player == "paper":
        if computer=="rock":
            print("You win!","Computer played:",computer,"You played:",player)
        else:
            print(loser,"Computer played:",computer,"You played:",player)
    elif player == "scissors":
        if computer == "rock":
            print(loser,"Computer played:",computer,"You played:",player)
        else:
            print("You win!","Computer played:",computer,"You played:",player)
    else:
        print("That´s not a valid play! Check your spelling!") # Fals man sich vertippt
        
        player=False        # sollte es nocht endlos weitergehen?
        computer=t[randint(0,2)]
        
       
     