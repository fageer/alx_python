def fibonacci_sequence(n):
    if n == 0:
        return [] 
    elif n == 1:
        return [0]
    fibunacci = [0, 1]
    for i in range(2, n):
        fibunacci = fibunacci + [fibunacci[-1] + fibunacci[-2]]
    return fibunacci
print(fibonacci_sequence(6))
print(fibonacci_sequence(1))
print(fibonacci_sequence(0))
print(fibonacci_sequence(20))
