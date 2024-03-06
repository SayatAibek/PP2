import os
def list(path):
    for root,dirs,files in os.walk(path):
        print("directory path: %s"%root)
        print("directory names: %s"%dirs)
        print("file names: %s"%files)
list('dir-and-files')