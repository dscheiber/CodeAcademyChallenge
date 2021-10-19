# 9. Just the numbers
# Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings. 
# The function should return a list with only the integers in the original list in the same order.

import random
import string

def makeRandomList():
    randomList = []
    length = random.randint(1, 20)
    for i in range(length):
        if random.randint(0,1) == 0:
            randomList.append(random.choice(string.ascii_lowercase))
        else:
            randomList.append(random.randint(0, 9))
    return randomList

def returnIntOnly(list):
    returnList = []
    for item in list:
        if type(item) == int:
            returnList.append(item)
    return returnList

list1 = makeRandomList()
output = returnIntOnly(list1)

print(list1)
print(output)

