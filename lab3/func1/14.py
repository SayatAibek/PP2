def solve(numheads, numlegs):
    rabbits=1
    chickens=numheads-1
    while rabbits<numheads:
        if chickens*2+rabbits*4==numlegs:
            return rabbits , chickens
        else: rabbits=rabbits+1
        chickens=chickens-1

def histogram(list):
    for x in list:
        print("*"*x)
    return ""

def vol(int):
    volume=(4/3)*3.14*int**3
    return volume

print(solve(35,94))
print(vol(10))
print(histogram([1,2,3]))