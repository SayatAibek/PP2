#task 1
def converte(grams):
    ounces = 28.3495231 * grams
    return ounces

#task 2
def calculate(fahrenheit):
    c=float((5/9)*(fahrenheit-32))
    return c

#task 3 
def solve(numheads, numlegs):
    rabbits=1
    chickens=numheads-1
    while rabbits<numheads:
        if chickens*2+rabbits*4==numlegs:
            return rabbits , chickens
        else: rabbits=rabbits+1
        chickens=chickens-1


#task 4  NEPRAVILNO
def filter_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def Prime_list(numbers):
    prime_numbers = [number for number in numbers if filter_prime(number)]
    return prime_numbers

num_list = [1, 2, 15, 9, 13, 100, 11, 19, 23, 31]
res = Prime_list(num_list)
print(res)

#task 5
from itertools import permutations

def print_permutations(string):
    
    perm_set = set(permutations(string))
    
    print(f"All string permutations '{string}':")
    for perm in perm_set:
        print(''.join(perm))

user_input = input("Enter the string: ")

print_permutations(user_input)

#task 6
def rev(str):
    x=str.split()
    y=x[::-1]
    return " ".join(y)


#task 7
def has33(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 3 and nums[i + 1] == 3:
      return True
  return False

#task 8
def spy_game(nums):
    for i in range(len(nums)- 1):
        if nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7:
            return True
    return False

user_list = [1,0,2,4,0,5,7]
answer = spy_game(user_list)
if answer:
    print("True")
else:
    print("False")

#task 9
def vol(int):
    volume=(4/3)*3.14*int**3
    return volume

#task 10
def unique(list):
    list.sort()
    list2=[]
    if list[-1]!=list[-2]:
            list2.insert(0,list[-1])
    for i in range(1,len(list)-1):
        if list[i]!=list[i-1] and list[i]!=list[i+1]:
            list2.insert(-1,list[i])
    return list2
#task 11
def palindrome(str):
    x=len(str)-1
    for i in range(0,len(str)-1):
        if str[i]!=str[x]:
            return 0
        x=x-1
        return 1
    
#task 12
def histogram(list):
    for x in list:
        print("*"*x)
    return ""
  

#task 13
def game():
    import random
    print("Hello! What is your name?")
    name=input()
    print("Well, " + name + ", I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    guesses=0
    x=random.randint(1,20)
    while guesses<19:
        guess=int(input())
        if guess==x:
            guesses=guesses+1
            print("Good job, " + name + "! You guessed my number in " + str(guesses) + "guesses!")
            return ""
        elif guess < x :
            print("Your guess is too low.")
            print("Take a guess.")
            guesses=guesses+1
        elif guess > x :
            print("Your guess is too large.")
            print("Take a guess.")
            guesses=guesses+1

