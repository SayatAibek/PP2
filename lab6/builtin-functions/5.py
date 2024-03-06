def t_or_f(tuplee):
    return all(tuplee)
print(t_or_f((True,True,False)))
print(t_or_f((True,True,True)))
print(t_or_f((False,False,False)))
