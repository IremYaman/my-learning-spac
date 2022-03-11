import random

def randomValue():
    x = [ "rock", "paper", "scissors" ] 
    value = x[random.randint(0,2)]
    return value

def rules(a,b,c,d):
    if (a=="rock" and b=="paper") or (a=="paper" and b=="rock"):
        print("Paper wins.")
        if a=="paper":
            print("You won this round.")
            c.append(1)
        elif b=="paper":
            print("Computer won this round.")
            d.append(1)
    elif (a=="rock" and b=="scissors") or (a=="scissors" and b=="rock"):
        print("Rock wins.")
        if a=="rock":
            print("You won this round.")
            c.append(1)
        elif b=="rock":
            print("Computer won this round.")
            d.append(1)
    elif (a=="paper" and b=="scissors") or (a=="scissors" and b=="paper"):
        print("Scissors wins.")
        if a=="scissors":
            print("You won this round.")
            c.append(1)
        elif b=="scissors":
            print("Computer won this round.")
            d.append(1)
    elif (a=="rock" and b=="rock"):
        print("Draw.")
    elif (a=="paper" and b=="paper"):
        print("Draw.")
    elif (a=="scissors" and b=="scissors"):
        print("Draw.")
    else:
        print("Wrong value.")
    
    
def game():
    healthPoint = 3
    player = []
    computer = []
    while healthPoint > 0:
        healthPoint -= 1
        x = randomValue()
        y = input("Rock, paper, scissors: ").lower()
        print (f"Computer: {x}")
        z = rules(y,x,player,computer)
        if healthPoint == 0:
            print("Game over.")
            playerScore = len(player)
            computerScore = len(computer)
            if playerScore > computerScore:
                print(f"Your score: {playerScore}")
                print(f"Computer's score: {computerScore}")
                print("You won!")
            elif computerScore > playerScore:
                print(f"Your score: {playerScore}")
                print(f"Computer's score: {computerScore}")
                print("Computer won.")
            elif playerScore == computerScore:
                print(f"Your score: {playerScore}")
                print(f"Computer's score: {computerScore}")
                print("Draw.")
        

game()


