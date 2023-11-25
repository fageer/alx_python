for i in range(100):
    if i < 99:
        print("{:02}".format(i), end=", ")
    else: 
        print("{:02}\n".format(i))
