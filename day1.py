
print("Hello")
#x = 10
#print(x)

#y = 100
#print(y)

# Operator - oprator can be used to performed the mathematical operation

# Arithmetic operation :->

# Addition - + 
# Subtraction - - 
# Multiplication - *
# Division   - /
# Remainder - %

# program 1
#s=10
#t=20

#print(s+t)
#print(s-t)
#print(s*t)
#print(s/t)
#print(s%t)

# program 2
#q = 100
#r = 20

#print(q+r)
#print(q-r)
#print(q*r)
#print(q/r)
#print(q%r)

# function --- fuction is a block of code its only run when function is called 
# function is define in a def keyword

def Calulator (a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)

    Calulator(12,9)

# Program 3

# function without parameter and without return type
def addA() :
    print(10+10)
    addA()

# function with parameter and without return type 

def addB(x,y):
    print(x+y)
addB(12,3)
addB(1,3)
addB(11,3)


# function with parameter and with return 
# 100 - shown
# 100 - given

def addC(x,y):
    return x + y
e = addC(24,5)
print(e)
print(e + e)
print(e * e)











