import re 
def upper_and_lower(s):
    x=re.findall(r'[A-Z][a-z]+',s)
    return x
print(upper_and_lower("One two Three fOur fivE"))