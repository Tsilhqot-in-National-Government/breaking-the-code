# pure.py
age = 10

vitals = {"age": 10}

def pureGrowOlder(startingAge,timePassedInYears):
    return startingAge + timePassedInYears

def globalGrowOlder(timePassedInYears):
    global age
    age += timePassedInYears

def sideEffectsGrowOlder(vitals,timePassedInYears):
    vitals["age"] += timePassedInYears

print("before call to pureGrowOlder")
print(age)
pureGrowOlder(age,3)
print("after call to pureGrowOlder")
print(age)

print("before call to globalGrowOlder")
print(age)
globalGrowOlder(3)
print("after call to globalGrowOlder")
print(age)

print("before call to sideEffectsOlder")
print(vitals["age"])
sideEffectsGrowOlder(vitals,3)
print("after call to sideEffectsGrowOlder")
print(vitals["age"])

# how I would do it
age = pureGrowOlder(age,3)

