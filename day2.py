# introvert    # extrovert
# calm           loud
# less outing    more outing
# less social    more social
# Human - 
# Properties - weight , height , color 
# Methods   - walk() , talk()

# Vehicle 
# Properties -  color , regNo , type , model 
# method     - start() , stop()

# Bank acc
# Propeties - accNo , accType , bal , IFSC
# Method - deposit() , withdrawl()

# Variable  & Types of variable

a = 10
print(a)
print(type(a))
# 10 , -10 , 0

b = 20.5
print(b)
print(type(b))
# 12.5 , -12.5 , 0.45

c = True
print(c)
print(type(c))
# True or False

d = "Hello"
print(d)
print(type(d))
#"A", "a", '#', "$$","FWEr34543ra@#$", " "

# Operator ----> operator are used to perform a mathematical operator
# syntax :-
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)

# 1.Arithmetic operator

# program 1

print(10+20)
print(10-20)
print(10*20)
print(10/20)
print(10%20)

# 2.Comparision operator
 # entity < entity ====> boolean ====> True or False
# < , > , <= , >= ,== ,!= 

print(6 > 3)
print(6 < 3)
print(6 >= 3)
print(6 <= 3)
print(6 >= 6)
print(6 <= 6)
print(6 != 6)
print(7 == 7)
print(8 !="8")

# 3.Logical operator

# and  
# True  and True   =====> True
# False and True   =====> False
# True  and False  =====> False
# False and False  =====> False

print(5 == 5 and 6 == 6)
print(7 == 8 and 9 == 9)
print(6 == 6 and 8 == 9)
print(8 == 9 and 9 == 8)

# or

# True  and True   =====> true
# False and True   =====> true
# True  and False  =====> true
# False and False  =====> False

print(5 == 5 or 6 == 6)
print(7 == 8 or 9 == 9)
print(6 == 6 or 8 == 9)
print(8 == 9 or 9 == 8)

# not -----> invert the output
# not true ==> False
# not false ==> true

print(not(100<50)or(200<100)) 
print(not(6<3 or 3>6))

# 4.Assignment operator
x = 99.96
print(x)

# 5.Membership operator
# in 
# not in
a=["apple","mango","orange"]
b=["apple","mango","orange"]
c = a
print (b not in a)
print(c in a)
print( a in b)
print(a in b)
