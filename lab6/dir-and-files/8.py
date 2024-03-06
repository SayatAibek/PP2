import os
def delete(path):
    if not os.path.exists(path):
        return "the path does not exist"
    else:
        os.remove(path)
    return "deleted"
