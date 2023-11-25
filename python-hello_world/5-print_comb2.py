for i in range(100):
    if i == 99:
        print("{}\n".format(i))
        break
    print("{:02d}".format(i),end=", ")
