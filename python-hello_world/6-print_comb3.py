for i in range(1, 10):
    for j in range(i, 10):
        if i < 9:
            print("{:02d}, ".format(j), end="")
        elif i == 9 and j == 9:
            print("{:02d}".format(j))