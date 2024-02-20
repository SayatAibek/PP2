def ntoi(n):
    for i in range(n,0,-1):
        yield i
for x in ntoi(10):
    print(x)