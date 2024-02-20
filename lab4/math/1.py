import math
#task 1
def degree_to_radian():
    a=float(input())
    return float(a * 0.0174533)
print(degree_to_radian())

#task 2
def area_of_trapezoid():
    h=input("Height: ")
    a=input("Base, first value: ")
    b=input("Base, second value: ")
    return float((h*(a+b))/2)

#task 3
def polygon():
    n=int(input("number of sides: "))
    a=float(input("the length of a side: "))
    return math.ceil((n*a**2)/(4*(1/math.tan(math.pi/n))))

#task 4
def parallelogram():
    b=float(input("Length of base: "))
    h=float(input("Height of parallelogram: "))
    return float(b*h)