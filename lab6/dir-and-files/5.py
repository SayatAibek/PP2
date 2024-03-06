import os
def list_to_file(list,file):
    f=open(file,'w')
    for i in list:
        f.write(i+'\n')
    f.close()
    f=open(file,'r')
    return f.read()