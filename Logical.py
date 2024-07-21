"""
Logical Operator in Python
and, or, Not

phy = 67
Chem = 92
"""
phy = int(input("Enter Physics Marks = "))
chem = int(input("Enter Chemistry Marks = "))
if phy > 33 and chem > 33:
    print("Pass")
else :
    print("Fail")

p = int(input("Enter Physics Marks = "))
c = int(input("Enter Chemistry Marks = "))
if p > 33 or c > 33:
    print("Pass")
else :
    print("Fail")
