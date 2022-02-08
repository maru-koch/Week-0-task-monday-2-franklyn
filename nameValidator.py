def nameValidator(name):

    if not name.isalpha():
        return "Invalid name"

    try:
        firstName, lastName = name.split(' ')
        print(lastName)
   
    except ValueError as err:
        print("Single or more than two names not allowed")

nameValidator("N7okocha Frank9yn")