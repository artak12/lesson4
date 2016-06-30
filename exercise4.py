def f():
    file = 'data.txt'
    f=open('data.txt')
    long = ''
    for line in f:
        print(line)
    print(len(line))

    if len(line) > len(long):
        long=line
        print("# =", len(long))
        print(long)
    return


f()