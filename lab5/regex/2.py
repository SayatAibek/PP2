import re
def two_or_three(s):
    x=r'^ab{2,3}'
    return bool(re.match(x,s))
print(two_or_three("abc"))
print(two_or_three("abbb"))