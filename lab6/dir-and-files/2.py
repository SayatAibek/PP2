import os
def check(path):
    if not os.path.exists(path):
        return "path does not exist"
    else:
        print('path exists')
        if os.access(path,os.R_OK):
            print("path is readable")
        else:
            print("path is not readable")
        
        if os.access(path,os.W_OK):
            print("path is writable")
        else:
            print("path is not writable")

        if os.access(path, os.X_OK):
            print("path is executable")
        else:
            print("path is not executable")
        return ""
