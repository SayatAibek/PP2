import re
def zero_or_more_b(s):
    x=r'^ab*'
    return bool(re.match(x,s))
print(zero_or_more_b("abb"))
print(zero_or_more_b("bb"))