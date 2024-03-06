import os
def check(path):
    if os.path.exists(path):
        dir = os.path.dirname(path)
        name=os.path.basename(path)
        return f"directory : {dir}  ,  filename : {name}"
    else:
        return f"path {path} does not exist"
path = 'dir-and-files'
print(check(path))