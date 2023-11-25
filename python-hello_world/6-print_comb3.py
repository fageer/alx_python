for i in range(1, 10):
    for j in range(i + 1, 10):
        if i != j:
            print("{:01d}{:01d}, ".format(i, j), end="")
print("\b\b\n")
