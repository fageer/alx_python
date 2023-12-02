def no_c(my_string):
    new = ""
    for char in my_string:
        if char.lower() != 'c':
            new += char
    return new
