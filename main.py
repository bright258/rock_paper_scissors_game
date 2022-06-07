
import random 

print("Welcome to the ROCK, PAPER, SCISSORS GAME ")
user = input("Enter an option, \n R for 'rock', P for 'paper', S for 'scissors': ").upper()
list1 = ["R", "P", "S"]
comp = random.choice(list1)
print(f'Player ({user}) : CPU ({comp})')



def roll(user,comp):
    
    if (user == "R") and (comp == 'S'):
        print ("player wins")
    elif (user == "S") and (comp == "R"):
        print ("CPU wins")

    elif user == comp :
        print("there's a tie")

    elif (user == "S") and (comp == "P"):
        print ("player wins")
    elif (user == "P") and (comp == "S"):
        print("CPU wins")
    
    elif (user == "R") and (comp == "P"):
        print ("CPU wins")


    elif (user == "P") and (comp == "R"):
        print ("player wins")

    else:
        pass
           

        
if user not in list1:
    
    while True:
        print('INVALID RESPONSE, try again...')
        user = input("Enter an option, \n R for 'rock', P for 'paper', S for 'scissors': ").upper()
        comp = random.choice(list1)
        print(f'Player ({user}) : CPU ({comp})')
        
        
        if user in list1:
            
            break


if user == comp:
    while True:
        print('There is a tie, try again...')
        user = input("Enter an option, \n R for 'rock', P for 'paper', S for 'scissors': ").upper()
        comp = random.choice(list1)
        print(f'Player ({user}) : CPU ({comp})')
        if user not in list1:
        
            while True:
                print('INVALID RESPONSE, try again...')
                user = input("Enter an option, \n R for 'rock', P for 'paper', S for 'scissors': ").upper()
                comp = random.choice(list1)
                print(f'Player ({user}) : CPU ({comp})')
                
                if user in list1:
                    
                    break
            
        elif user in list1:
            
            break
        break
        

roll(user,comp);
