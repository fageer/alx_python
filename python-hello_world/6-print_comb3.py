for i in range(10):
    for j in range(i + 1, 10):
        if i != 0:
            print(", ", end="")
        print("{:02d}{:02d}".format(i, j), end="")
print()