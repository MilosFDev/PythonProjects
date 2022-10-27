#Code is designed to be rant only once, I didn't add many functions due to making code as simple as possible 
import random #imports library which we will need to gen random number
x = str(input("rock, paper, scissors: ")) # This is for the input which in this case is string
if x == "paper" :
    print(f'you have chosen {x}')         #f'' this makes us write our usual string + input directly here
    x = 1                                 #We converted variable to integer which will be more clear later
elif x == "rock":
    print(f'you have chosen {x}')
    x = 2
elif x == "scissors":
    print(f'you have chosen {x}')
    x = 3

y = random.randint(1,3)                   #We added random.randint which generated random integer and that value is stored in our variable
if y == 1:                                
    print(f'Enemy has chosen paper')      #Just normal output
elif y == 2:
    print(f'Enemy has chosen rock')
elif y == 3:
    print(f'Enemy has chosen scissors')

if x == 1 and y == 1:
    print ('Draw, run the code again')    #This is just code which is needed here
elif x == 2 and y == 1:                   #I'm sure better solution exists but this is the one I made myself
    print('You lost ,Try again')          #You can add while loop here too, but as I said, I aimed at simplicity, not at making code short
elif x == 3 and y == 1:
    print('Congrats, you won')
elif x == 1 and y == 2:
    print('Congrats, you won')
elif x == 2 and y == 2:
    print('Draw, run the code again')
elif x == 3 and y == 2: 
    print ('You lost ,Try again')
elif x == 1 and y == 3:
    print('You lost ,Try again')
elif x == 2 and y == 3:
    print('Congrats, you won')
elif x == 3 and y == 3:
    print('Draw, try again')
