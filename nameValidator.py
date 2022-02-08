
def nameValidator(name):

        if any(letter.isdigit() for letter in name): return "Invalid Name"

        else: 
            try: 
                firstName, lastName = name.split(' ')

                if len(firstName) >= 5 and len(lastName) >= 5: 

                    return firstName + ' ' + lastName
                
                else: return "First or last name less than five character"
        
            except ValueError as err:
                print("Single or more than two names not allowed:", err)

print(nameValidator("maruche farhgoeouse"))