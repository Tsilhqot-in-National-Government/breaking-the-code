def printZeroTo(n):
    currentNumber = 0
    while currentNumber <= n:
        print(currentNumber)
        currentNumber += 1
    return True

def logger(n):
    print("Logging the numbers from one to " + str(n))
    return printZeroTo(n)

if(logger(10)): print("Logger ran fine!")