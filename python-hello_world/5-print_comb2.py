for i in range(100):
    if i < 99:
        print("{:02d}, ".format(i), end="")
    else: 
        print("{:02d}\n".format(i))
