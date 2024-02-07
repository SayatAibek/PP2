#task 1
class upp:
    def __init__(self):
        self.string=""
    def getstring(self):
        self.string = input()
    def printstring(self):
        print(self.string.upper())
st=upp()
st.getstring()
st.printstring()

#task 2
class shape:
    def area():
        return 0
class square(shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        return self.length**2

#task 3
class shape:
    def area():
        return 0
class rectangle(shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    
#task 4
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.x , self.y)
        return ""
    def move(self,change_x,change_y):
        self.x+=change_x
        self.y+=change_y
        return ""
    def dist(self,x2,y2):
        return ((self.x-x2)**2+(self.y-y2)**2)**0.5
'''s=point(2,4)
print(s.dist(2,10))'''

#task 5 
class banc_account:
    def  __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance
    def deposit(self,plus):
        return self.balance + plus
    def withdraw(self,minuse):
        if minuse>self.balance:
            return
        else:return self.balance-minuse