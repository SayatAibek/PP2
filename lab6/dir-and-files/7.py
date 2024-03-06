import os
def copy(first,second):
    with open(first,'r') as f1:
        with open(second,'w') as f2:
            f2.write(f1.read())
    return ""
