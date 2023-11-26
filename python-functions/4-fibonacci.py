def fibonacci_sequence(n):
    fibunacci = [0, 1]
    while len(fibunacci) < n:
            anothernum = fibunacci[-1] + fibunacci[-2]
            fibunacci = fibunacci + [anothernum]
    return fibunacci[:n]
