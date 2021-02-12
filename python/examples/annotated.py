def createUser(id: int,name: str, age: int,isEmployee: bool = False):
    '''
    Parameters:
    id: id for the user
    name: User's first and last name (middle omitted)
    age: User's age as number (not string)
    isEmployee: Whether or not the user works for the organization
    '''
    return {
        "id": id,
        "name": name,
        "age": age,
        "isEmployee": isEmployee
    }

help(createUser)

createUser("jkadf",11,"34","yes")