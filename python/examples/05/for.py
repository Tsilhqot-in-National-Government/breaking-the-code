print("loop over range")
for i in range(8):
    print(i)

print("loop over string")
coolMove = "Cartwheel"
for c in coolMove:
    print(c)

print("loop over list")
myList = ["hi","bye","see ya"]
for message in myList:
    print(message)

print("loop over tuple")
myTuple = (8,9,12)
for number in myTuple:
    print(number)

print("loop over set")
mySet = {"x","y","z"}
for val in mySet:
    print(val)

print("loop over dict keys")
myDict = {
    "name": "Joe", #("name","Joe")
    "age": "26", #("age","26")
    "position": "Quarterback" #("position","Quarterback")
}
for prop in myDict:
    print(prop)

print("loop over key values")
for value in myDict.values():
    print(value)

print("loop over keys and values in dict")
for k,v in myDict.items():
    print(k + ": " + v)

print("What's going on here?")

