#2 numbers only, not repeatable - for now
import math

def sum(x, y): 
    return x + y

def sub(x, y): 
    return x - y

def multi(x, y):  
    return x * y

def div(x, y): 
    return x / y    

def percent(x, y):
    return 100 * (x / y)

     
x=float(input("Choose: 1. (+,-,/,*,%) ; 2. square root ; 3.  "))
if x == 1:
    choice = input("Choose : 1. summary, 2. subtraction, 3. multiplication, 4. division , 5. percent ")  
    if choice in ('1', '2' , '3' , '4' , '5'):                                          
        num1 = float(input("Enter first number: "))                                    
        num2 = float(input("Enter second number: "))                                   
        
        if choice == '1':                                                   
            print(sum(x, y)(num1, num2))
            
        elif choice == '2':
            print(sub(x, y)(num1, num2))
            
        elif choice == '3':
            print(multi(num1, num2))
            
        elif choice == '4':
            print(div(x, y)(num1, num2))
            
        elif choice == '5':
            print(percent(x, y)(num1, num2))
            
if x == 2:
    num1 = float(input("Choose which number you want to square root of: "))
    print(math.sqrt(num1))

if x == 3:
    num1 = int(input("Enter which number you want square of : "))
    num2 = int(input("Exponenial power of? : "))
    square = int(pow(num1, num2))
    print(square)

if x > 3:
    print("start again")

#Code explanation
#import math // We need that library for our square root function
#int(input) // Converts input to integer
