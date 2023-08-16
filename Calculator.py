
#Calculator
def add(num1, num2): #Add Function
  return num1 + num2 #Add Function

def subtract(num1, num2): #Subtract Function
  return num1 - num2 #Subtract Function

def multiply(num1, num2): #Multiply Function
  return num1 * num2 #Multiply Function

def divide(num1, num2): #Divide Function
  return num1 / num2 #Divide Function

operations = { #Operations Dictionary
  "+": add, #Add Function
  "-": subtract, #Subtract Function
  "*": multiply, #Multiply Function
  "/": divide #Divide Function
}

def calculator(): #Calculator Function
  should_continue = True #Should Continue
  while should_continue: #While Should Continue
    num1 = float(input("What's the first number?: ")) #Num1
    for symbol in operations: #For Symbol in Operations Dictionary
      print(symbol) #Print Symbol
    operation_symbol = input("Pick an operation: ") #Operation Symbol
    num2 = float(input("What's the next number?: ")) #Num2
    calculation_function = operations[operation_symbol] #Calculation Function
    answer = calculation_function(num1, num2) #Answer
    print(f"{num1} {operation_symbol} {num2} = {answer}") #Print Answer

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y': #If input is equal to 'y'
      num1 = answer #Num1
    else: #Else
      should_continue = False #Should Continue is False
      calculator() #Calculator

calculator() #Calculator Function
