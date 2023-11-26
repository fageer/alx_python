for i in range(10):
    for j in range(i + 1, 10):
        print("{:01d}{:01d}".format(i, j), end=", ")
        if i == 8 and j == 9:
            print("{:01d}{:01d}".format(i, j), end="\n")
print("\b\n")
