#This code is maden for shopping, it should be really simple
#I included list here, It will be simple yet good
ingredients = ['salt','sugar','butter','eggs','garlic','water','olive oil','milk','flour','onion']
salt,sugar,butter,eggs,garlic,water,olive_oil,milk,flour,onion=1.0, 1.2, 1.5, 0.2, 2.2, 0.5, 2.3, 1.7, 1.5, 1.3
confirmation=input('Welcome to FailedDevs shop, what would you like to buy?\n Say "yes" if you would like to continue \n Say "no" if you are just passing by\n  :')
bill=0
order=''
if confirmation == 'yes':
    menu_confirmation=input('Would you like to see the menu:')
    if menu_confirmation == 'yes':
        print(ingredients[0],'=',salt,'$')
        print(ingredients[1],'=',sugar,'$')
        print(ingredients[2],'=',butter,'$')
        print(ingredients[3],'=',eggs,'$')
        print(ingredients[4],'=',garlic,'$')
        print(ingredients[5],'=',water,'$')
        print(ingredients[6],'=',olive_oil,'$')
        print(ingredients[7],'=',milk,'$')
        print(ingredients[8],'=',flour,'$')
        print(ingredients[9],'=',onion,'$')
        while True:
            order=input('What would you like to buy?')
            if order in ingredients:
                if order == 'salt':
                    order_confirmation=input('You selected salt, do you want to continue?\n If yes, enter "yes" again :')
                    if order_confirmation == 'yes':
                        quantity0=float(input(f'How many salt would you like to buy?\n Current price of salt is {salt}\n Enter quantity:'))
                        bill=bill+quantity0*salt
                        print(f'Your bill is currently : {bill}$')
                elif order == 'sugar':
                    order_confirmation=input('You selected sugar, do you want to continue?\n If yes, enter "yes" again :')
                    if order_confirmation == 'yes':
                        quantity1=float(input(f'How many sugar would you like to buy?\n Current price of salt is {sugar}\n Enter quantity:'))
                        bill=bill+quantity1*sugar
                        print(f'Your bill is currently : {bill}$')
                elif order == 'butter':
                    order_confirmation=input('You selected butter, do you want to continue?\n If yes, enter "yes" again :')
                    if order_confirmation == 'yes':
                        quantity2=float(input(f'How many butter would you like to buy?\n Current price of salt is {butter}\n Enter quantity:'))
                        bill=bill+quantity2*butter
                        print(f'Your bill is currently : {bill}$')    
                elif order == 'eggs':
                    order_confirmation=input('You selected eggs, do you want to continue?\n If yes, enter "yes" again :')
                    if order_confirmation == 'yes':
                        quantity3=float(input(f'How many eggs would you like to buy?\n Current price of eggs is {eggs}\n Enter quantity:'))
                        bill=bill+quantity3*eggs
                        print(f'Your bill is currently : {bill}$')  
                elif order == 'garlic':
                    order_confirmation=input('You selected garlic, do you want to continue?\n If yes, enter "yes" again :')
                    if order_confirmation == 'yes':
                        quantity4=float(input(f'How many garlic would you like to buy?\n Current price of garlic is {garlic}\n Enter quantity:'))
                        bill=bill+quantity4*garlic
                        print(f'Your bill is currently : {bill}$')  
                elif order == 'water':
                    order_confirmation=input('You selected water, do you want to continue?\n If yes, enter "yes" again :')
                    if order_confirmation == 'yes':
                        quantity5=float(input(f'How many water would you like to buy?\n Current price of water is {water}\n Enter quantity:'))
                        bill=bill+quantity5*water
                        print(f'Your bill is currently : {bill}$')  
                elif order == 'olive_oil':
                    order_confirmation=input('You selected olive oil, do you want to continue?\n If yes, enter "yes" again :')
                    if order_confirmation == 'yes':
                        quantity6=float(input(f'How much olive oil would you like to buy?\n Current price of olive oil is {olive_oil}\n Enter quantity:'))
                        bill=bill+quantity6*olive_oil
                        print(f'Your bill is currently : {bill}')
                elif order == 'milk':
                    order_confirmation=input('You selected milk, do you want to continue?\n If yes, enter "yes" again :')
                    if order_confirmation == 'yes':
                        quantity7=float(input(f'How much milk would you like to buy?\n Current price of milk is {milk}\n Enter quantity:'))
                        bill=bill+quantity7*milk
                        print(f'Your bill is currently : {bill}')
                elif order == 'flour':
                    order_confirmation=input('You selected flour, do you want to continue?\n If yes, enter "yes" again :')
                    if order_confirmation == 'yes':
                        quantity8=float(input(f'How much flour would you like to buy?\n Current price of flour is {flour}\n Enter quantity:'))
                        bill=bill+quantity8*flour
                        print(f'Your bill is currently : {bill}')
                elif order == 'onion':
                    order_confirmation=input('You selected onion, do you want to continue?\n If yes, enter "yes" again :')
                    if order_confirmation == 'yes':
                        quantity9=float(input(f'How many onions would you like to buy?\n Current price of onions is {onion}\n Enter quantity:'))
                        bill=bill+quantity9*onion
                        print(f'Your bill is currently : {bill}')
            else:
                break
                
        print('Thanks for visiting our shop')
        if bill>0:
            print(f'Thanks for buying here, your bill is {bill} ')
        #I could add payment method here, I mean something really simple which would rely on lenght and some other shit but I think it's kinda unnecessary

else:
    print('I hope you will visit our shop soon, have fun!')
    exit()
#CODE EXPLANATION
#(f'text{variable})// it is supposed to add that variable's value into string
#list[0] // prints first item from list
#marko,nikola = 1,2 // you can put multiple variables in one line , here marko will have value 1 and nikola value 2
# float(input('text goes here)) // converts input to float