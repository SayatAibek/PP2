import re
def convert(text):
    return ''.join(x.capitalize() for x in text.split('_'))
print(convert("one_two_three"))