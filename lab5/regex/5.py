import re 
def ab(s):
    x=re.match(r'\ba.+b\b',s)
    return x
s=["abc","adb","acb","aqwertyb"]
for x in s:
    print(f'{x}:{ab(x)}')