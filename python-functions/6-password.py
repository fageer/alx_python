def validate_password(password):
    Lower = False
    Upper = False
    Digit = False
    if ' ' in password:
        return False
    elif len(password) < 8:
        return False
    else:
        for char in password:
            if char.islower():
                Lower = True
            elif char.isupper():
                Upper = True
            elif char.isdigit():
                Digit = True
            if Lower == True and Upper == True and Digit == True:
                return True 
    return False
