def fibonacci_sequence(n):
    if n == 0:
        return [] 
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    fibunacci = [0, 1]
    for i in range(2, n):
        anothernum = fibunacci[-1] + fibunacci[-2]
        fibunacci = fibunacci + [anothernum]
    return fibunacci
