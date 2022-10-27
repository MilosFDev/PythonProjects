import random
x = str(input("rock, paper, scissors: "))
if x == "paper" :
    print(f'you have chosen {x}')
    x = 1
elif x == "rock":
    print(f'you have chosen {x}')
    x = 2
elif x == "scissors":
    print(f'you have chosen {x}')
    x = 3

y = random.randint(1,3)
if y == 1:
    print(f'Enemy has chosen paper')
elif y == 2:
    print(f'Enemy has chosen rock')
elif y == 3:
    print(f'Enemy has chosen scissors')

if x == 1 and y == 1:
    print ('Draw, run the code again')
elif x == 2 and y == 1:
    print('You lost ,Try again')
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