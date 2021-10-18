# 6. Are the Xs equal to the Os?
# Create a Python function that accepts a string. This function should count the number of Xs and 
# the number of Os in the string. It should then return a boolean value of either True or False.

# If the count of Xs and Os are equal, then the function should return True. 
# If the count isn't the same, it should return False. If there are no Xs or Os in the string, 
# it should also return True because 0 equals 0. The string can contain any type and number of characters.

def receiveInput():
    inputString = input("Enter a string with Xs and Os if you'd like, because I can compare their counts. That is my purpose. Thanks. \n")
    inputString = str(inputString).lower()
    return inputString

def stringCompare(string):
    if string.count("x") == string.count("o"):
        return True
    else:
        return None

userInput = receiveInput()
comparison = stringCompare(userInput)

print(type(comparison))
print(comparison)