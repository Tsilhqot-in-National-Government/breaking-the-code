def returnNone():
    print("This function explicitly returns None")
    return None

print("Type of return value: ",type(returnNone()))

def noReturn():
    print("This function has no explicit return statement.")
    
print("Type of return value: ",type(noReturn()))

def justReturn():
    print("This function has only the keyword return with no value.")
    return

print("Type of return value: ",type(justReturn()))


def shortCircuitedAddTwo(x):
    print("This function's return statement prevents execution of additional code.")
    output = x + 2
    return output
    output = x + 3
    print("I'll never see the light of day.")
def getSize(x):
    if(x<100):
        return "small"
    return "big"
print(shortCircuitedAddTwo(6))
