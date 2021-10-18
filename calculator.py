# 7. Create a calculator function
# Write a Python function that accepts three parameters. The first parameter is an integer. 
# The second is one of the following mathematical operators: +, -, /, or *. The third parameter will also be an integer.

# The function should perform a calculation and return the results. 
# For example, if the function is passed 6 and 4, it should return 24.

##the following two lines are necessary to translate the string input for operator into an operator function
import operator
operationsDict = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}

##gets inputs from the user with input validation, returns a list to be ingested by calculator function
def calculatorInputs():
    integerValidation = None
    while integerValidation == None:
        try:
            getInteger = int(getInteger)
            integerValidation = True
        except:
            getInteger = input("What is your first value to be used in the calculation? \n")
    
    operatorValidation = None
    while operatorValidation == None:
        try:
            if getOperator == "+" or getOperator == "-" or getOperator == "*" or getOperator == "/":
                operatorValidation = True
        except:
            getOperator = input("What is your operator to be used in the calculation? (+ - * /) \n")

    secondIntegerValidation = None
    while secondIntegerValidation == None:
        try:
            getSecondInteger = int(getSecondInteger)
            secondIntegerValidation = True
        except:
            getSecondInteger = input("What is your second value to be used in the calculation? \n")
    
    return [getInteger, getOperator, getSecondInteger]


##calculates the inputs, uses a dictionary as a lookup to translate the operator string to an operator function
def calculator(integer, operator, secondInteger):
    return operationsDict[operator](integer, secondInteger)


##executed; i don't like how i use list indices but it works
inputs = calculatorInputs()
output = calculator(inputs[0], inputs[1], inputs[2])
print(output)