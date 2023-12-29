def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Error: Division by zero"
    
def calculator():
    x = float(input("Enter the first number : "))
    y = float(input("Enter the second number : "))
    operation=input("print the number of the operation\n 1-Add \n 2-Subtract \n 3-Multiply \n 4-Divide \n")
    
    if operation == '1':
        result = add(x,y)
    elif operation == '2':
        result = subtract(x,y)
    elif operation == '3':
        result = multiply(x,y)
    elif operation == '4':
        result = divide(x,y)
    else:
        result = "Error"
    print("Result : ", result)
calculator()