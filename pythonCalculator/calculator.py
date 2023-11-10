# Addition function
def calcAdd(x, y):
    z = x + y
    return z

# Subtraction Function
def calcSub(x, y):
    z = x - y
    return z

#Multiplication Function
def calcMultiply(x, y):
    z = x * y
    return z

#Division Function
def calcDivide(x, y):
    z = x / y
    return z
    
def mainCalculator():
    while True:
        try:
            x = float(input("Enter the first number: "))
            operator = input("Choose the operation (+, -, *, /): ")
            y = float(input("Enter the second number: "))

            if operator == "+":
                result = calcAdd(x, y)
                
            elif operator == "-":
                result = calcSub(x, y)
    
            elif operator == "*":
                result = calcMultiply(x, y)
            
            elif operator == "/":
                if y == 0:
                    print("Value error, division by zero is not allowed.")
                    continue
                else:
                    result = calcDivide(x, y)
            
            else:
                print("Invalid operator. Only choose between +, -, *, or /.")
                break
            print(f"The answer is: {result}")
            
            choice = input("Do you want to do another calculation? (y/n): ").lower()
            if choice != "y":
                print("Thank you for using my simple calculator. The program will now exit.")
                break
        
        # Deals with the non numerical inputs
        except ValueError:
            print("Value error, please enter numeric values only.")
        
mainCalculator()