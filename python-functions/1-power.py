def pow(a,b):
    if b == 0:
        return 1
    elif b > 0:
        return a * pow(a,b-1)
    else:
        return 1 / pow(a,-b)
