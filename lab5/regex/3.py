import re
def underscore(s):
    x=re.findall(r'[a-z][a-z]*_[a-z][a-z]*',s)
    return x
print(underscore("text one_two and text three_four a_b"))