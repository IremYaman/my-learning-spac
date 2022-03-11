import random

def welcome():
    print("Welcome...")
    while True:
        x = input("Wanna play some Chō-Han Bakuchi?(yes/no): ").lower().strip()
        if x == "yes":
            print("Alright, let's start...")
            return x
            break
        elif x == "no":
            print("Your choice, see you later.")
            return None
            break
        else:   
            print("You typed wrong. ")  
        



def buyin():
    while True:
        buyIn = int(input("Enter the amount of buy-in you want to enter the game(100$-10000$):  "))
        if 100 <= buyIn <= 10000:
            return buyIn
            break
        else:   
            print("You entered a wrong amount. ")  
        

def playerBet(a):
    while True:
        x = int(input("Enter the amount of bet you want to play with: "))
        if 0 < x <= a:
            print("Good luck!")
            return x
            break
        else:
            print("You can't bet this amount. ")


def playerChoice():
    while True:
        x = input("Odd or even?: ").capitalize().strip()    
        if x == "Odd":
            return x
            break
        elif x == "Even":
            return x
            break
        else:
            print("You typed wrong. ")

            
def dice():
    x = random.randint(1,6)
    return x


def oddEven(a):
    if a%2 == 0:
        return "Even"
    else:
        return "Odd"


def rules(a,b,d):
    if a==b:
        print("Congrats, you won!")
        return d*2
    elif a!=b:
        print("You lost.")
        return -d
    

def tryQuit():
    while True:
        x = input("Wanna try again or quit?(try/quit): ").lower().strip()
        if x == "try":
            return True
            break
        elif x == "quit":
            print("See you later.")
            return False
            break
        else:
            print("You typed wrong.")



def quitMore():
    while True:
        x = input("Wanna buy-in more or quit?(buyin/quit): ").lower().strip()
        if x == "buyin":                                           
            print("Let's try again...")
            return True
            break
        elif x == "quit":
            print("See you later.")
            return False
            break
        else:
            print("You typed wrong.")


def game():
    x = welcome()
    if x is not None:
        a = True
        money = buyin()
        while a:
            firstDice = dice()
            secondDice = dice()
            sumDice = firstDice + secondDice
            bet= playerBet(money)
            choice = playerChoice()
            print(f"First dice: {firstDice}, second dice: {secondDice}")
            print(f"Sum of two dice: {sumDice}")
            diceResult = oddEven(sumDice)
            print(diceResult)
            money += rules(choice,diceResult,bet)
            print(f"Current cashier: {money}")
            if money > 0:
                a = tryQuit()
            else: 
                print("You don't have any money left in your cashier. ")
                a = quitMore()
                if a == True:
                    more = buyin()
                    money += more
                        



game()
        






