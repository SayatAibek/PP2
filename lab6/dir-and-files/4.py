import os
def count(path):
    y=0
    text_file=open(path,'r')
    for x in text_file:
        print(x)
        y=y+1
    return y
