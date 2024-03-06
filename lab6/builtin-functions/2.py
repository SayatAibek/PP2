def cnt(string):
    lower=0  
    upper=0
    for x in string:
        if x.islower()==True:
            lower=lower+1
        elif x.isupper()==True:
            upper=upper+1
    return upper,lower
print(cnt("My name is KBTU"))