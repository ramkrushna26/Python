#!/bin/python

print("====Raised exception====")
def printBox(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("'symbol' should of length 1!")
    if (width < 2) or (height < 2):
        raise Exception("Width and Height should be greater than equal to 2!")

    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


printBox('*', 10, 5)
#printBox('**', 15, 5)
#printBox('&', 1, 1)
'''
# writing raised exception to error file
import traceback

try:
    raise Exception("Raised exception")
except:
    errorFile = open("error.log", 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()

'''

print("====assert statements====")
# assert statements for program errors and not for users

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchlight(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        if intersection[key] == 'yellow':
            intersection[key] = 'red'
        if intersection[key] == 'red':
            intersection[key] = 'green'
        assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(market_2nd)
switchlight(market_2nd)
print(market_2nd)
