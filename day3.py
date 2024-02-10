# conditional statements 

# one and multiple outcomes

# numT > 0 and numT <= 5  --- 10 % discount
# numT > 5 and numT <= 10 --- 20 % discount
# numT > 10               --- 30 % discount
# syntax :--
# if condition:
#     statements

# program 1

numT = 5

if numT > 0 and numT <= 5:
    print("10 % discount")
if numT > 5 and numT <= 10:
    print("20 % discount")
if numT > 10:
    print("30 % discount")

# elif 
# syntax :--
    # if condition :
    #     statements
    # elif condition 2 :
    #       statements 
    #     else
    #         statements

# program 2

numT2 =  -17
if numT2 >= 0 and numT2 <= 5:
    print("5 % discount")
elif numT2 > 5 and numT2 <= 10:
    print("10 % discount")
elif numT2 > 10:
    print("20 % discounr")
else:
    print("incorrect input")

# program 3

marks = 55

# if marks > 90:
#     print("Grade A")
# if marks >= 75:
#     print("Grade B")
# if marks >= 65:
#     print("Grade C")

# program 4    

if marks > 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 65:
    print("Grade C")
else:
    print("try again ...!")


# program 5 
a = 10 
b = 50

if a > b:
    print("a is greater")
else:
    print("b is greater")

# program 6 

x1 = 1000 
x2 = 5000
x3 = 20000

if x1 > x2 and x1 > x3:
    print("x1 is greater")
elif x2 > x1 and x2 > x3:
    print("x2 is greater")
else:
    print("x3 is greater")




