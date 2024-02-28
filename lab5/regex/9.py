import re
def ins(txt):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
print(ins("OneTwoThree"))