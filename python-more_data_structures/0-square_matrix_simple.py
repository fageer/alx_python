def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j * j)
        new_matrix.append(row)
    return (new_matrix)
        