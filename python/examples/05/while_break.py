def printZeroTo(n):
    currentNumber = 0
    while True:
        print(currentNumber)
        currentNumber += 1
        if(currentNumber == n): break
    return True

def logger(n):
    print("Logging the numbers from one to " + str(n))
    return printZeroTo(n)

if(logger(10)): print("Logger ran fine!")