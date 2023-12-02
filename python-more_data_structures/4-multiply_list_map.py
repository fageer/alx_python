def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))

my_list = [1, 2, 3, 4, 6]
new_list = multiply_list_map(my_list, 4)
print(new_list)
print(my_list)
