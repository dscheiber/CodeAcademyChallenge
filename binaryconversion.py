# 3. Convert a decimal number into binary
# Write a function in Python that accepts a decimal number and returns the equivalent binary number. 
# To make this simple, the decimal number will always be less than 1,024, 
# so the binary number returned will always be less than ten digits long.


##author note: ok, so i hardly understand binary besides the crash course i received in calculating binary vs IP address for
##properly establishing VPC subnets. with that said, i checked my work against a calculator and it's all good.
##i didn't need to make it simple and did not limit it to <1024.

## simple ask for number w input validation.
def getNumber():
    number = 0
    numberValidation = None
    while numberValidation == None:
        number = input('Choose a number to be converted to binary. \n')
        try:
            number = int(number)
            if number >= 0: #and number <= 1024: ##removed bc i didn't need
                numberValidation = True
            else:
                print('Not a valid input.')
        except:
            print('Not a valid input.')
    return number

## determines the number of digits necessary for the final value. builds a list of n^2 multiples such that it can be used
## for determining the actual digits later on
def digitDetermination(number):
    digit = 2
    binaryLength = [0]
    while number >= digit:
        #print(number, digit)
        binaryLength.append(digit)
        digit += digit
    binaryLength.reverse()
    return binaryLength

## starting from the "left most digit", calculates the digit by determining the remainder of current number and n^2 multiple
def calculateBinaryValues(number, binaryLength):
    binaryList = []
    for value in binaryLength:
        remainder = number - value
        if remainder >= 0 and number != 0:
            binaryList.append('1')
            number = remainder
        else:
            binaryList.append('0')
    return binaryList
    
def mainLoop():
    value = getNumber()
    testDigits = digitDetermination(value)
    binaryValues = calculateBinaryValues(value, testDigits)
    binaryString = ''.join(binaryValues)
    return binaryString

print(mainLoop())
