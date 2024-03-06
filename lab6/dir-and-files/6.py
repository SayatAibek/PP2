import string

def create_files():
    al = string.ascii_uppercase
    for let in al:
        file_name = let + ".txt"
        f=open(file_name, 'w')
create_files()