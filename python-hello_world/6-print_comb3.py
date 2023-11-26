for i in range(10):
    for j in range(i + 1, 10):
        print("{:02d}, {:02d}".format(i, j), end=", ")
        if i == 8 and j == 9:
            print("{:02d}{:02d}".format(i, j))
print("\n")
