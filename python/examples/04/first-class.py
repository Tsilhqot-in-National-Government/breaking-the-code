def applyFunction(f,data):
    return f(data)

def printMe(s):
    print(s)

def subtractThree(x):
    print(x - 3)

def doubleMe(x):
    print(2*x)

listOfFunctions = {
    "print":printMe,
    "subtract":subtractThree,
    "double":doubleMe
    }

for functionName in listOfFunctions.keys():
    f = listOfFunctions[functionName]
    print("Applying function ",functionName," to 4")
    applyFunction(f,4)

def selectOperation(method):
    if method in listOfFunctions:
        return listOfFunctions[method]

currentOperation = "print"

printMethod = selectOperation(currentOperation)
printMethod("Whoa!")
