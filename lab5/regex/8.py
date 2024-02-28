import re

def spl_upp(s):
    return re.findall('[A-Z][^A-Z]*', s)

s = str(input())
res = spl_upp(s)
print("Original string:", s)
print("Split result:", res)