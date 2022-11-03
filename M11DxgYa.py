import math

def sum(x, y):  #definisana funkcija sabiranje
    return x + y

def sub(x, y): #definisana funckija oduzimnanje
    return x - y

def multi(x, y):  
    return x * y

def div(x, y): 
    return x / y    

def percent(x, y):
    return 100 * (x / y)

     
x=float(input("Choose: 1. (+,-,/,*,%) ; 2. square root ; 3.  "))
if x == 1:
    choice = input("Choose : 1. summary, 2. subtraction, 3. multiplication, 4. division: ")  #biramo racunsku operaciju
    if choice in ('1', '2' , '3' , '4' , '5'):                                           #operacije oznacili sa brojevima radi lakseg koda
        num1 = float(input("Enter first number: "))                                    #broj 1. stavljen float radi brojeva sa decimalama
        num2 = float(input("Enter second number: "))                                   #broj 2. stavljen float radi brojeva sa decimalama
        
        if odabir == '1':                                                   
            print(plus(num1, num2))
            
        elif odabir == '2':
            print(minus(num1, num2))
            
        elif odabir == '3':
            print(dijelenje(num1, num2))
            
        elif odabir == '4':
            print(puta(num1, num2))
            
        elif odabir == '5':
            print(procenat(num1, num2))
            
if x == 2:
    num1 = float(input("Izaberi broj koji ces da korijenujes : "))
    print(math.sqrt(num1))

if x == 3:
    num1 = int(input("unesi broj : "))
    num2 = int(input("na koji stepen ? : "))
    square = int(pow(num1, num2))
    print(square)

if x > 3:
    print("pokreni ispocetka")
    


