from functools import reduce

def myltp(num):
    res = reduce(lambda x, y: x * y, num)
    return res

num_list = [2, 5, 8, 3]
print(myltp(num_list))