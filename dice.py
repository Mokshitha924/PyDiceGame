import random
min=1
max=6
ComputerScore=0
PlayerScore=0
inPlay=True
x=20
while x<10:
    test=random.randint(min,max)
    print(test)
    x+=1
def gamePlay():
    global inPlay
    global ComputerScore
    global PlayerScore
    while inPlay:
        global ComputerScore
        global PlayerScore
        player=random.randint(min,max)
        computer=random.randint(min,max)
        print(f"You Got{player}vs Computer {computer}")
        if player==computer:
            print("Tie Game")
        elif player>computer:
            print("You won")
            PlayerScore+=1
        elif player<computer:
            print("Computer won")
            ComputerScore+=1
        inPlay=input("Roll Again? (yes/no)")
        if inPlay=="no":
            print("Game Over")
            print(f"Computer Score:{ComputerScore} vs Player Score:{PlayerScore}")
            break
gamePlay()
print("Game over")
print(f"Computer Score:{ComputerScore} vs Player Score:{PlayerScore}")
