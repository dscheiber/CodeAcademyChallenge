# 10. Repeat the characters
# Create a Python function that accepts a string. The function should return a string, with each character 
# in the original string doubled. 

# If you send the function "now" as a parameter, 
# it should return "nnooww," and if you send "123a!", it should return "112233aa!!".

def inputString():
    string = input('Enter a string for which each character will be doubled. \n')
    return string

def stringDoubler(string):
    doubledStringList = []
    for character in string:
        doubledStringList.append(character)
        doubledStringList.append(character)
    doubledString = ''.join(doubledStringList)
    return doubledString

input = inputString()
output = stringDoubler(input)
print(output)