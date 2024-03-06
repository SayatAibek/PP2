import math
import time

def invoke(num, millisec):
    time.sleep(millisec / 1000)
    square = math.sqrt(num)
    return f"Square root of {num} after {millisec} milliseconds is {square}"
print(invoke(25100,2123))