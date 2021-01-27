john = {
    "height": 72,
    "weight": 185,
    "name": "John"
}
def getVitals(person):
    return person['name'], person['height'], person['weight']
    # (.,.,.) would also work

johnVitals = getVitals(john)
print("type of johnVitals: ")
print(type(johnVitals))
print("John's vitals: ")
print(johnVitals)
