import re
def replace(s):
    a=r'[;, ]'
    x=re.sub(a,"?",s)
    return x
print(replace("one two three"))