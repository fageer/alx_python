def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j, num in enumerate(i):
            if j == len(i) - 1:
                print("{:d}".format(num), end="")
            else:
                print("{:d} ".format(num), end="")
        print()
