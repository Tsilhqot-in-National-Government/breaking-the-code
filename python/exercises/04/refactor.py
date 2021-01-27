john = {
    "age":22,
    "name": "John",
    "title": "janitor"
}

sue = {
    "age": 44,
    "name": "Sue",
    "title": "boss"
}

sarah = {
    "age": 25,
    "name": "Sarah",
    "title": "IT Architect"
}

employees = [john,sue,sarah]

# Refactor from here on. Don't touch the code before.

for e in employees:
    print(e['name'])
    print(e['age'])
    print(e['title'])

print("Applying promotions.")

john["age"] += 1
sue["age"] += 1
sarah["age"] += 1

john["title"] = "boss"
sue["title"] = "retired"
sarah["title"] = "GIS Team Lead"

for e in employees:
    print(e['name'])
    print(e['age'])
    print(e['title'])