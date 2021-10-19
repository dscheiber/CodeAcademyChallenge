# 8. Give me the discount
# Create a function in Python that accepts two parameters. The first should be the full price of an item as an integer. 
# The second should be the discount percentage as an integer.

# The function should return the price of the item after the discount has been applied. 
# For example, if the price is 100 and the discount is 20, the function should return 80.

def discountCalculatorInputs():

    inputPriceValidation = None
    while inputPriceValidation == None:
        try:
            price = int(price)
            inputPriceValidation = True
        except:
            price = input("What is the starting price? \n")

    inputDiscountValidation = None
    while inputDiscountValidation == None:
        try:
            discount = int(discount)
            if discount >= 0 and discount <= 100:
                inputDiscountValidation = True
            else:
                discount = input("What is the discount percentage? \n")
        except:
            discount = input("What is the discount percentage? \n")

    return [price, discount]

def discountCalculation(price, discount):
    actualPrice = float(price - (price * discount/100))
    return actualPrice

inputs = discountCalculatorInputs()
outputs = discountCalculation(inputs[0], inputs[1])

print(outputs)
    